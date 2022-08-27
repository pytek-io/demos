from itertools import count
from operator import itemgetter

from anyio import Event
from reflect import Window, get_window, js, create_observable
from reflect.connection import record_connection
from reflect.utils import anext
from reflect_aggrid import AgGridColumn, AgGridReact
from reflect_antd import message
from reflect_html import div
from reflect_rcdock import DockLayout, DropDirection
from reflect_utils.common import dummy_connection, read_pickles, ws_connection_manager

from .config import (
    CLIENT,
    DEFINITIONS,
    DEPLOYMENT,
    PRIORITY_GROUP,
    RUNNING_TASKS_DEF,
    SESSION,
    WORKER,
)

CSS = [
    "static/antd.css",  # tab names formatting
]
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
        # avoiding to alter input so that we can reuse it...
        definition = definition.copy()
        definition["children"] = children
    else:
        if definition.get("hide", False):
            width = 0
        else:
            width = definition.get("width", None)
            if width is None:
                raise Exception(f"Missing width in column definition: {definition}")
    return AgGridColumn(**definition), width


def create_columns(definitions):
    columns, widths = zip(*[create_column(definition) for definition in definitions])
    return columns, sum(widths)


def create_grid(
    definition,
    is_leaf,
    extra_args,
    name=None,
    on_didmount=None,
    on_unmount=None,
):
    name = name or definition["name"]
    columns, width = create_columns(definition["columns"])
    getContextMenuItems = definition.get("getContextMenuItems", None)
    if getContextMenuItems:
        getContextMenuItems = js("createContextMenu", getContextMenuItems)

    grid = AgGridReact(
        columns,
        getRowNodeId=js("id"),
        defaultColDef=dict(resizable=True),
        getContextMenuItems=getContextMenuItems,
        className="ag-theme-balham",
        **extra_args,
    )
    static_fields = definition.get("static_fields", None) or [
        column["field"] for column in definition["columns"]
    ]
    update_fields = definition.get("update_fields", static_fields)
    title = create_observable(name, key="tab title")

    title_component = div([title])
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
        title_component  # this needs to be kept alive in the closure
        if update:
            await grid.applyTransactionAsync(update)
        else:
            print("ignoring update", update)

    content = div(
        grid,
        style=dict(height=800, width=width + 200),
        componentDidMount=on_didmount,
        componentWillUnmount=on_unmount,
    )
    return title_component, content, update_grid


class Application:
    def __init__(self, window: Window):
        self.window: Window = window
        self.counter = count()
        self.nb_tabs_created = 0
        self.grids_ready = Event()
        session_extra_arguments = dict(
            autoGroupColumnDef={
                "headerName": "Priority Group / Session",
                "cellRendererParams": {
                    "suppressCount": True,
                },
                "minWidth": 220,
            },
            groupDefaultExpanded=-1,  # expand all groups by default
            getDataPath=js("fetch_attribute", "priority_group_path"),
            treeData=True,
        )
        self.updaters, self.main_grids = {}, {}
        for info_type, definition in DEFINITIONS.items():
            title, grid, updater = create_grid(
                definition,
                is_leaf=itemgetter("is_session") if info_type == SESSION else None,
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
                    {
                        "tabs": self.create_main_tab(SESSION),
                    },
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
        self.dock_layout = DockLayout(
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
            print("UpdateSubscription", subscribe, session_id)
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
                    print("calling message")
                    (message.success if success else message.error)(description)
                else:
                    print("received", msg)

    async def main(self, connection_manager):
        await self.grids_ready.wait()
        async with connection_manager as self.server_connection:
            self.window.start_soon(self.process_client_messages)
            self.window.start_soon(self.process_server_messages)
            for info_type in DEFINITIONS:
                await self.server_connection.send(["UpdateSubscription", True, info_type])

    async def insert_panel(self, title, component):
        # FIXME: use reflect_utils.common.create_tab_inserter instead
        panel_id = (await self.dock_layout.saveLayout())["dockbox"]["children"][0]["id"]
        await self.dock_layout.dockMove(
            self.create_tab(
                title,
                component,
                closable=True,
            ),
            panel_id,
            DropDirection.MIDDLE,
        )

    async def process_client_messages(self):
        async for code, args in self.window.client_connection:
            if code == "DisplayRunningTasks":
                session_id = args[0]
                if session_id in self.updaters:
                    continue  # we don't want to support multiple instances of the same session...
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
                del (
                    title,
                    component,
                )  # making sure the frame does not keep a hard ref (this is to avoid spurious warnings when closing the last opened tab)
            else:
                if code == "UpdateAttribute":
                    is_session, rest = split_sequence(args, 1)
                    record_type = SESSION if is_session[0] else PRIORITY_GROUP
                    message = [code, record_type] + rest
                elif code == "TerminateSession":
                    message = [
                        code,
                        args[0],
                        "Session terminated from web client",
                    ]
                else:
                    message = [code] + args
                await self.server_connection.send(["RequestToMaster", 0, message])


async def app():
    window = get_window()
    argument = window.hash()
    # quick fix to get this demos working in app_explorer (should be fixed by a smarter hash implementation)
    # argument = json.loads(argument) if argument else {}
    argument = {}
    uri, archive = argument.get("uri", None), argument.get(
        "archive", "demos/dispatch/replay.pick"
    )
    app = Application(window=window)
    # server_connection_host, http_port = "0.0.0.0", 30000
    # uri = "ws://{}:{}/ws".format(server_connection_host, http_port)
    # uri = "wss://30000-beige-clam-nmcnkydt.ws-eu08.gitpod.io/ws"
    if uri:
        connection = ws_connection_manager(
            uri=uri, task_group=window.task_group, number_messages=True
        )
        if archive:
            connection = record_connection(connection, open(archive, "wb"))
    else:
        connection = dummy_connection(read_pickles(open(archive, "rb")))

    window.start_soon(app.main, connection)
    return app.dock_layout
