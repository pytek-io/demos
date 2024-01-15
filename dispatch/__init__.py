import itertools
import json
import operator

import anyio
import render as r
import render_aggrid as aggrid
import render_antd as antd
import render_html as html
import render_rcdock as rcdock
from asyncstdlib.builtins import anext

from demos.connection import ws_connection_manager

from .config import (CLIENT_DEF, DEPLOYMENT_DEF, RUNNING_TASKS_DEF, SESSION,
                     WORKER_DEF, create_session_columns,
                     session_extra_arguments)
from .utils import dummy_connection, read_pickles, record_connection

TITLE = "Dispatch"
CREATION = "C"
UPDATE = "U"
DELETE = "D"


def create_column(definition):
    children = definition.get("children", None)
    if children:
        children, width = create_columns(children)
        definition = definition.copy()
        definition["children"] = children
    elif definition.get("hide", False):
        width = 0
    else:
        width = definition["width"]
    return aggrid.AgGridColumn(**definition), width


def create_columns(definitions):
    columns, widths = zip(*[create_column(definition) for definition in definitions])
    return columns, sum(widths)


class Application:
    def __init__(self, window: r.Window):
        self.window = window
        self.counter = itertools.count()
        self.updaters = {}
        self.ready = anyio.Event()
        self.pending_grids = [
            grid_def["subject"] for grid_def in [WORKER_DEF, CLIENT_DEF, DEPLOYMENT_DEF]
        ] + [SESSION]
        self.create_context_menu_items = r.js_arrow(
            "context_menu_items", aggrid.CREATE_CONTEXT_MENU_ITEMS_JS
        )
        defaultLayout = {
            "dockbox": {
                "mode": "vertical",
                "children": [
                    {
                        "tabs": [
                            self.create_tab(
                                *self.create_grid(
                                    create_session_columns(
                                        self.session_attributes_update
                                    ),
                                    is_leaf=operator.itemgetter("is_session"),
                                    extra_args=session_extra_arguments,
                                    context_menu_callback=self.session_context_menu,
                                )
                            )
                        ]
                    },
                    {
                        "mode": "horizontal",
                        "children": [
                            {
                                "tabs": [
                                    self.create_tab(
                                        *self.create_grid(
                                            DEPLOYMENT_DEF,
                                            context_menu_callback=self.deployment_context_menu,
                                        )
                                    )
                                ]
                            },
                            {"tabs": [self.create_tab(*self.create_grid(WORKER_DEF))]},
                            {"tabs": [self.create_tab(*self.create_grid(CLIENT_DEF))]},
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

    async def session_context_menu(self, code, session_id):
        if code == "DisplayRunningTasks":
            if session_id not in self.updaters:
                await self.insert_panel(
                    *self.create_grid(
                        RUNNING_TASKS_DEF,
                        name=f"Session{session_id}",
                        subject=session_id,
                    )
                )
        else:
            if code == "TerminateSession":
                message = [code, session_id, "Session terminated from web client"]
            else:
                message = [code, session_id]
            await self.server_connection.send(["RequestToMaster", 0, message])

    def deployment_context_menu(self, *args):
        print(*args)

    async def session_attributes_update(self, code, session_id):
        print(code, session_id)
        return
        await self.server_connection.send(["RequestToMaster", 0, message])

    def create_mount_callback(self, subject, updater):
        def result():
            self.server_connection.send_nowait(
                ["UpdateSubscription", bool(updater), subject]
            )
            if updater:
                self.updaters[subject] = updater
                if subject in self.pending_grids:
                    self.pending_grids.remove(subject)
                    if not self.pending_grids:
                        self.ready.set()
            else:
                self.updaters.pop(subject)

        return result

    def create_grid(
        self,
        definition=None,
        is_leaf=None,
        extra_args=None,
        name=None,
        subject=None,
        context_menu_callback=None,
    ):
        name = name or definition["name"]
        subject = subject or definition["subject"]
        columns, width = create_columns(definition["columns"])
        if context_menu_callback:
            getContextMenuItems = self.create_context_menu_items(
                self.window.register_callback(context_menu_callback, hard_ref=True),
                definition["context_menu_items"],
            )
        else:
            getContextMenuItems = None
        grid = aggrid.AgGridReact(
            columns,
            getRowId=r.js_arrow("data.id", "({data}) => data.id"),
            defaultColDef={"resizable": True},
            getContextMenuItems=getContextMenuItems,
            **extra_args or {},
        )
        static_fields = definition.get("static_fields", None) or [
            column["field"] for column in definition["columns"]
        ]
        update_fields = definition.get("update_fields", static_fields)
        title_obs = r.ObservableValue(name, key=f"tab {subject}")
        title = html.div([title_obs])
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
            title_obs.set(f"{name} ({row_count})")
            if update:
                await grid.applyTransactionAsync(update)
            else:
                print("ignoring update", update)

        return title, html.div(
            grid,
            style={"height": 800, "width": width + 200},
            componentDidMount=self.create_mount_callback(subject, update_grid),
            componentWillUnmount=self.create_mount_callback(subject, None),
        )

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

    async def process_server_messages(self):
        _, grid_name = await anext(self.server_connection)
        self.window.update_title(f"{grid_name} grid")
        await self.ready.wait()
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

    async def insert_panel(self, title, component):
        panel_id = (await self.dock_layout.saveLayout())["dockbox"]["children"][0]["id"]
        await self.dock_layout.dockMove(
            self.create_tab(title, component, closable=True),
            panel_id,
            rcdock.DropDirection.MIDDLE,
        )


async def main(app: Application, connection_manager):
    async with connection_manager as app.server_connection:
        app.window.start_soon(app.process_server_messages)


async def app(window: r.Window):
    arguments = json.loads(window.hash()) if window.hash() else {}
    archive = arguments.get("archive", None)
    server_connection_host = arguments.get("server", None)
    http_port = arguments.get("port", None)
    if server_connection_host and http_port:
        connection_manager = ws_connection_manager(
            uri=f"ws://{server_connection_host}:{http_port}/ws",
            task_group=window.task_group,
            number_messages=True,
        )
        if archive:
            connection_manager = record_connection(
                connection_manager, open(archive, "wb")
            )
    elif archive:
        connection_manager = dummy_connection(read_pickles(open(archive, "rb")))
    else:
        return antd.TypographyText(
            "Either a connection or an archive path must be provided."
        )
    app = Application(window)
    window.start_soon(main, app, connection_manager)
    return app.dock_layout
