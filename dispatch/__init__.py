import itertools
import json
import operator

import anyio
import reflect_aggrid as aggrid
import reflect_antd as antd
import reflect_html as html
import reflect_rcdock as rcdock
import reflect_utils as utils

import reflect as r

from .config import (CLIENT, DEFINITIONS, DEPLOYMENT, PRIORITY_GROUP,
                     RUNNING_TASKS_DEF, SESSION, WORKER)
from .utils import anext, dummy_connection, read_pickles, record_connection

CSS = ["static/antd.css"]
TITLE = "Dispatch"
CREATION = "C"
UPDATE = "U"
DELETE = "D"


def split_sequence(sequence, index):
    return sequence[:index], sequence[index:]


def create_column(definition):
    children = definition.get("children", None)
    if children:
        children, width = create_columns(children)
        definition = definition.copy()
        definition["children"] = children
    elif definition.get("hide", False):
        width = 0
    else:
        width = definition.get("width", None)
        if width is None:
            raise Exception(f"Missing width in column definition: {definition}")
    return aggrid.AgGridColumn(**definition), width


def create_columns(definitions):
    columns, widths = zip(*[create_column(definition) for definition in definitions])
    return columns, sum(widths)


def create_grid(
    definition, is_leaf, extra_args, name=None, on_didmount=None, on_unmount=None
):
    name = name or definition["name"]
    columns, width = create_columns(definition["columns"])
    getContextMenuItems = definition.get("getContextMenuItems", None)
    if getContextMenuItems:
        getContextMenuItems = r.js("createContextMenu", getContextMenuItems)
    grid = aggrid.AgGridReact(
        columns,
        getRowNodeId=r.js("id"),
        defaultColDef=dict(resizable=True),
        getContextMenuItems=getContextMenuItems,
        className="ag-theme-balham",
        **extra_args,
    )
    static_fields = definition.get("static_fields", None) or [
        column["field"] for column in definition["columns"]
    ]
    update_fields = definition.get("update_fields", static_fields)
    title = r.create_observable(name, key="tab title")
    title_component = html.div([title])
    row_count = 0
    rows = {}

    async def update_grid(msg):
        nonlocal row_count
        update = None
        msg_type, row_type, row_id, details = msg
        if msg_type == CREATION:
            record = rows[row_id] = dict(zip(static_fields, details), id=row_id)
            update = {"add": [record]}
            row_count += 1 if is_leaf is None or is_leaf(record) else 0
        elif msg_type == UPDATE:
            rows[row_id].update(zip(update_fields, details))
            update = {"update": [rows[row_id]]}
        else:
            assert msg_type == DELETE, f"unknown message type {msg_type}"
            record = rows.pop(row_id, None)
            if record:
                row_count -= 1 if is_leaf is None or is_leaf(record) else 0
                update = {"remove": [{"id": row_id}]}
        title.set(f"{name} ({row_count})")
        title_component
        if update:
            await grid.applyTransactionAsync(update)
        else:
            print("ignoring update", update)

    content = html.div(
        grid,
        style=dict(height=800, width=width + 200),
        componentDidMount=on_didmount,
        componentWillUnmount=on_unmount,
    )
    return title_component, content, update_grid


class Application:
    def __init__(self, window: r.Window):
        self.window = window
        self.counter = itertools.count()
        self.nb_tabs_created = 0
        self.grids_ready = anyio.Event()
        session_extra_arguments = dict(
            autoGroupColumnDef={
                "headerName": "Priority Group / Session",
                "cellRendererParams": {"suppressCount": True},
                "minWidth": 220,
            },
            groupDefaultExpanded=-1,
            getDataPath=r.js("fetch_attribute", "priority_group_path"),
            treeData=True,
        )
        self.updaters, self.main_grids = {}, {}
        for info_type, definition in DEFINITIONS.items():
            title, grid, updater = create_grid(
                definition,
                is_leaf=operator.itemgetter("is_session")
                if info_type == SESSION
                else None,
                extra_args=session_extra_arguments if info_type == SESSION else {},
                on_didmount=self.on_grid_did_mount,
            )
            self.updaters[info_type], self.main_grids[info_type] = updater, (
                title,
                grid,
            )
        defaultLayout = {
            "dockbox": {
                "mode": "vertical",
                "children": [
                    {"tabs": self.create_main_tab(SESSION)},
                    {
                        "mode": "horizontal",
                        "children": [
                            {"tabs": self.create_main_tab(DEPLOYMENT)},
                            {"tabs": self.create_main_tab(WORKER)},
                            {"tabs": self.create_main_tab(CLIENT)},
                        ],
                    },
                ],
            }
        }
        self.dock_layout = rcdock.DockLayout(
            defaultLayout=defaultLayout,
            style={
                "position": "absolute",
                "left": 0,
                "top": 0,
                "right": 0,
                "bottom": 0,
            },
        )

    def on_grid_did_mount(self):
        self.nb_tabs_created -= 1
        if self.nb_tabs_created == 0:
            self.grids_ready.set()

    def create_tab(self, title, content, closable=False):
        return {
            "id": str(next(self.counter)),
            "title": title,
            "content": content,
            "cached": True,
            "minWidth": 30,
            "minHeight": 40,
            "closable": closable,
        }

    def create_mount_callback(self, session_id, subscribe):
        def result():
            self.server_connection.send_nowait(
                ["UpdateSubscription", subscribe, session_id]
            )
            if not subscribe:
                self.updaters.pop(session_id)

        return result

    def create_main_tab(self, info_type):
        self.nb_tabs_created += 1
        return [self.create_tab(*self.main_grids[info_type], closable=False)]

    async def process_server_messages(self):
        _, grid_name = await anext(self.server_connection)
        self.window.update_title(f"{grid_name} grid")
        async for msg in self.server_connection:
            if len(msg) == 4:
                msg_type, row_type, row_id, details = msg
                if row_type in self.updaters:
                    await self.updaters[row_type](msg)
                else:
                    print("ignoring", msg)
            elif len(msg) == 3:
                code, success, description = msg
                if code == "R":
                    (antd.message.success if success else antd.message.error)(
                        description
                    )
                else:
                    print("ignoring", msg)

    async def main(self, connection_manager):
        await self.grids_ready.wait()
        async with connection_manager as self.server_connection:
            self.window.start_soon(self.process_client_messages)
            self.window.start_soon(self.process_server_messages)
            for info_type in DEFINITIONS:
                await self.server_connection.send(
                    ["UpdateSubscription", True, info_type]
                )

    async def insert_panel(self, title, component):
        panel_id = (await self.dock_layout.saveLayout())["dockbox"]["children"][0]["id"]
        await self.dock_layout.dockMove(
            self.create_tab(title, component, closable=True),
            panel_id,
            rcdock.DropDirection.MIDDLE,
        )

    async def process_client_messages(self):
        async for code, args in self.window.client_connection:
            if code == "DisplayRunningTasks":
                session_id = args[0]
                if session_id in self.updaters:
                    continue
                title, component, updater = create_grid(
                    RUNNING_TASKS_DEF,
                    is_leaf=None,
                    extra_args={},
                    name="Running tasks",
                    on_didmount=self.create_mount_callback(session_id, True),
                    on_unmount=self.create_mount_callback(session_id, False),
                )
                self.updaters[session_id] = updater
                await self.insert_panel(title, component)
                del (title, component)
            else:
                if code == "UpdateAttribute":
                    is_session, rest = split_sequence(args, 1)
                    record_type = SESSION if is_session[0] else PRIORITY_GROUP
                    message = [code, record_type] + rest
                elif code == "TerminateSession":
                    message = [code, args[0], "Session terminated from web client"]
                else:
                    message = [code] + args
                await self.server_connection.send(["RequestToMaster", 0, message])


async def app(window: r.Window):
    arguments = json.loads(window.hash()) if window.hash() else {}
    archive = arguments.get("archive", None)
    server_connection_host = arguments.get("server", None)
    http_port = arguments.get("port", None)
    if server_connection_host and http_port:
        connection = utils.ws_connection_manager(
            uri=f"ws://{server_connection_host}:{http_port}/ws",
            task_group=window.task_group,
            number_messages=True,
        )
        if archive:
            connection = record_connection(connection, open(archive, "wb"))
    else:
        connection = dummy_connection(read_pickles(open(archive, "rb")))
    app = Application(window=window)
    window.start_soon(app.main, connection)
    return app.dock_layout
