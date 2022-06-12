"""Allows to quickly navigate between apps displaying code and preview."""

import os
from pathlib import Path

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
    base_path = get_window().hash() or str(
        Path(__file__).parent.parent.relative_to(Path(os.getcwd()))
    )
    filter_method = (
        lambda p: any(p.startswith(s) for s in ["__", "."]) and not p == "__init__.py"
    )
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
                    get_module_name(actual_path()), ""
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
                    height="100%",
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
                                    div(maybe_editor, style={"height": "100%"}),
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
                                            "overflow": "scroll",
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

    def nice_path():
        result = (actual_path() or "").replace(os.sep, ".")
        if result:
            result = result[:-3]
        if result.endswith("__init__"):
            result = result[:-9]
        return result

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
                            nice_path,
                            href=lambda: "/app/" + nice_path(),
                            target="_blank",
                            title=lambda: f"Launch {nice_path()}",
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
