"""Allows to quickly navigate between apps displaying code and preview."""
import os
import pathlib

import reflect_html as html
import reflect_monaco as monaco
import reflect_rcdock as rcdock
import reflect_utils

import reflect as r

TITLE = "App explorer"
ALMOST_BLACK = "#0f1724"


def call_if_callable(maybe_callable):
    return maybe_callable() if callable(maybe_callable) else maybe_callable


def app(window: r.Window):
    base_path = window.hash() or str(
        pathlib.Path(__file__).parent.parent.relative_to(pathlib.Path(os.getcwd()))
    )
    filter_method = (
        lambda p: any(p.startswith(s) for s in ["__", "."]) and not p == "__init__.py"
    )
    current_path, file_explorer = reflect_utils.create_file_explorer(
        base_path, folder_filter=filter_method, file_filter=filter_method
    )
    file_explorer.style.update({"paddingTop": 7, "paddingLeft": 10})
    def actual_path():
        if current_path():
            result = os.path.join(base_path, current_path())
            return None if os.path.isdir(result) else result

    relative_path = lambda: actual_path() or "No app selected"

    @r.memoize()
    def component_and_settings():
        actual_path_value = actual_path()
        if actual_path_value:
            extension = actual_path_value.rsplit(".", 1)[-1]
            if extension == "py":
                _success, _css, _title, component = reflect_utils.evaluate_demo_module(
                    reflect_utils.get_module_name(actual_path()), ""
                )
                return component
            elif extension in ["svg", "png", "gif"]:
                return html.img(src=actual_path_value)
            elif extension in ["md", "mdx"]:
                return reflect_utils.parse_md_doc(open(actual_path_value, "r").read())
            else:
                return html.div(None)

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
                return monaco.Editor(
                    defaultValue=open(actual_path(), "r").read(),
                    options=dict(
                        minimap={"enabled": False},
                        lineNumbers=True,
                        glyphMargin=False,
                        wordWrap=False,
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
                    "tabs": [
                        ({"title": base_path, "content": file_explorer, "closable": False})
                    ],
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
                                    html.div(maybe_editor, style={"height": "100%"}),
                                )
                            ],
                        },
                        {
                            "size": 1,
                            "tabs": [
                                (
                                    "Preview",
                                    html.div(
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
                                    html.div(
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

    return html.div(
        [
            html.div(
                [
                    html.div(
                        "App explorer",
                        style={
                            "padding": ".5rem",
                            "fontSize": "1.5rem",
                            "color": "white",
                            "marginLeft": "2rem",
                        },
                    ),
                    html.div(
                        lambda: html.a(
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
            rcdock.DockLayoutReflect(defaultLayout=defaultLayout, style={"flex": 2}),
        ],
        style={"display": "flex", "flexDirection": "column", "minHeight": "100%"},
    )
