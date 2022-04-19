"""Allows to quickly navigate between apps displaying code and preview."""

import os

from reflect import get_window, memoize
from reflect_html import a, div, img
from reflect_monaco import Editor as CodeEditor
from reflect_rcdock import DockLayoutReflect
from reflect_utils import create_file_explorer, evaluate_demo_module, get_module_name
from reflect_utils.md_parsing import parse_md_doc

TITLE = "App explorer"
ALMOST_BLACK = "#0f1724"


def call_if_callable(maybe_callable):
    return maybe_callable() if callable(maybe_callable) else maybe_callable


def app():
    base_path = get_window().hash()
    filter_method = lambda p: any(p.startswith(s) for s in ["__", "."])
    current_path, tree = create_file_explorer(
        base_path, folder_filter=filter_method, file_filter=filter_method
    )

    def actual_path():
        if current_path():
            result = os.path.join(base_path, current_path())
            return None if os.path.isdir(result) else result

    relative_path = lambda: actual_path() or "No app selected"

    @memoize()
    def component_and_settings():
        actual_path_value = actual_path()
        if actual_path_value:
            extension = actual_path_value.rsplit(".", 1)[-1]
            if extension == "py":
                _success, _css, _title, component = evaluate_demo_module(
                    get_module_name(actual_path()), {}
                )
                return component
            elif extension in ["svg", "png", "gif"]:
                return img(src=actual_path_value)
            elif extension == "md":
                return parse_md_doc(open(actual_path_value, "r").read())
            else:
                return div(None)

    def component():
        component_and_settings_value = component_and_settings()
        return (
            component_and_settings_value.content
            if hasattr(component_and_settings_value, "content")
            else component_and_settings_value
        )

    def settings():
        component_and_settings_value = component_and_settings()
        return (
            call_if_callable(component_and_settings_value.settings)
            if hasattr(component_and_settings_value, "settings")
            else "No settings to show"
        )

    def maybe_editor():
        if actual_path():
            try:
                return CodeEditor(
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
            except:
                pass

    defaultLayout = {
        "dockbox": {
            "mode": "horizontal",
            "children": [
                {
                    "size": 1,
                    "tabs": [("Apps", tree)],
                },
                {
                    "size": 3,
                    "mode": "vertical",
                    "children": [
                        {
                            "size": 2,
                            "tabs": [
                                (
                                    relative_path,
                                    div(maybe_editor),
                                ),
                            ],
                        },
                        {
                            "size": 1,
                            "tabs": [
                                (
                                    "Preview",
                                    div(
                                        component,
                                        style={
                                            "height": "inherit",
                                            "width": "inherit",
                                            "padding": 20,
                                        },
                                    ),
                                ),
                                (
                                    "Settings",
                                    div(
                                        settings,
                                        style={
                                            "height": "inherit",
                                            "width": "inherit",
                                            "padding": 20,
                                        },
                                    ),
                                ),
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
                            href=lambda: "/app/" + actual_path()[:-3]
                            if actual_path()
                            else None,
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
            DockLayoutReflect(
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
