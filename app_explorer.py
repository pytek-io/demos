"""This is a app allows to have quick look at apps."""

import os
from reflect import get_window
from reflect_html import div, a
from reflect_rcdock import DockLayout
from reflect_utils.common import create_file_explorer, evaluate_demo_module
from reflect_utils.misc import get_module_name
from reflect_monaco import Editor as CodeEditor


TITLE = "App explorer"
ALMOST_BLACK = "#0f1724"


def app():
    base_path = get_window().hash()
    counter = 0

    def create_tab(title, application):
        nonlocal counter
        counter += 1
        return {
            "id": str(counter),
            "title": div(title) if callable(title) else title,
            "content": application,
            "cached": True,
        }

    current_path, tree = create_file_explorer(
        base_path, folder_filter=lambda p: p.startswith("__")
    )
    def actual_path():
        if current_path():
            result = os.path.join(base_path, current_path())
            return None if os.path.isdir(result) else result
    relative_path = lambda: actual_path() or "No app selected"

    def component():
        if actual_path():
            _success, _css, _title, component = evaluate_demo_module(
                get_module_name(actual_path()), {}
            )
            return component

    editor = div(
        lambda: CodeEditor(
            defaultValue=open(actual_path(), "r").read(),
            options=dict(
                minimap={"enabled": False},
                lineNumbers=True,
                glyphMargin=False,
                wordWrap=True,
                readOnly=True,
            ),
            defaultLanguage="python",
            height=600,
        )
        if actual_path()
        else None
    )
    defaultLayout = {
        "dockbox": {
            "mode": "horizontal",
            "children": [
                {
                    "size": 1,
                    "tabs": [create_tab("Apps", tree)],
                },
                {
                    "size": 3,
                    "mode": "vertical",
                    "children": [
                        {
                            "size": 2,
                            "tabs": [
                                create_tab(
                                    relative_path,
                                    editor,
                                ),
                            ],
                        },
                        {
                            "size": 1,
                            "tabs": [
                                create_tab(
                                    "Preview",
                                    div(
                                        component,
                                        style={
                                            "padding": 20,
                                        },
                                    ),
                                )
                            ],
                        },
                    ],
                },
            ],
        }
    }
    return div(
        [
            div(
                [
                    div(
                        "App explorer",
                        style={
                            "padding": ".5rem",
                            "fontSize": "1.5rem",
                            "color": "white",
                            "marginLeft": "2rem",
                        },
                    ),
                    div(
                        lambda: a(
                            "launch",
                            href=lambda: "/app/" + actual_path(),
                            target="_blank",
                            title=lambda: f"Launch {actual_path()}",
                        )
                        if actual_path()
                        else None,
                        style={
                            "padding": ".5rem",
                            "fontSize": "1.0rem",
                            "color": "white",
                            "marginLeft": "auto",
                            "marginRight": "2rem",
                        },
                    ),
                ],
                style={
                    "backgroundColor": ALMOST_BLACK,
                    "display": "flex",
                    "alignItems": "center",
                },
            ),
            DockLayout(
                defaultLayout=defaultLayout,
                style={"flex": 2},
            ),
        ],
        style={
            "display": "flex",
            "flexDirection": "column",
            "minHeight": "100%",
        },
    )
