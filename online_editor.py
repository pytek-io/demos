import json
import os
import stat

import render as r
import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html
import render_rcdock as rcdock
import render_utils

from demos.ant import create_code_editor

TITLE = "Online Editor"
BASE_PATH = "demos"


def is_writable_file(file_path):
    """works even with sudo rights..."""
    return "w" in stat.filemode(os.lstat(file_path).st_mode)


def robust_open_file(file):
    try:
        return open(file).read().split("\n")
    except Exception as e:
        return [str(e)]


def create_editor(file, language, read_only):
    return create_code_editor(
        language,
        robust_open_file(file),
        lineNumbers=True,
        readOnly=read_only,
        height=600,
    )


def app(window: r.Window):
    arguments = (
        json.loads(window.hash()) if window.hash() else {"main": "demos/hello_world.py"}
    )
    main, css, kwargs = arguments["main"], arguments.get("css", []), {}
    window.add_css(css)
    main, kwargs = render_utils.decode_url(main)
    actual_file_path, language = render_utils.extract_file_path_and_language(main)
    editor = create_editor(actual_file_path, language, read_only=False)

    def delayed_component():
        window.hash()
        if language == "python":
            _success, css, title, component = render_utils.evaluate_demo_module(
                main, kwargs
            )
            if css:
                window.add_css(css)
            component = html.section(
                component,
                id="code-box-demo",
                className="code-box-demo",
                style={"height": "100%"},
            )
        else:
            component = render_utils.parse_md_doc(open(actual_file_path).read())
        return component

    title = "Preview"
    _, file_name = os.path.split(actual_file_path)
    defaultLayout = {
        "dockbox": {
            "mode": "vertical",
            "children": [
                {"tabs": [rcdock.create_tab(file_name, editor)]},
                {
                    "tabs": [
                        rcdock.create_tab(
                            title or file_name.split(".")[0],
                            html.div(
                                delayed_component,
                                style={
                                    "padding": 20,
                                    "overflow": "scroll",
                                    "height": "inherit",
                                },
                            ),
                        )
                    ]
                },
            ],
        }
    }
    dock_layout = rcdock.DockLayout(
        defaultLayout=defaultLayout,
        style={"position": "absolute", "left": 0, "top": 50, "right": 0, "bottom": 0},
    )
    insert_tab = rcdock.create_tab_inserter(dock_layout)
    create_file_visible = r.ObservableValue(False, key="create_file_visible")

    async def open_file(file):
        if file:
            file = os.path.join(BASE_PATH, file)
            _folder_path, file_name = os.path.split(file)
            editor = create_editor(
                file,
                render_utils.monaco_language_from_extension(file_name),
                read_only=True,
            )
            await insert_tab(file_name, editor)

    (
        file_selection_window,
        show_file_selection_window,
    ) = render_utils.create_file_chooser(
        BASE_PATH, title="Select file to open", on_ok=open_file
    )
    name, extension = file_name.rsplit(".", 1) if "." in file_name else file_name, ".py"
    default_new_file_name = f"{name}_test.{extension}"
    new_file_name_input = antd.Input(defaultValue=default_new_file_name)

    async def reload():
        if not is_writable_file(actual_file_path):
            create_file_visible.set(True)
        else:
            if not os.path.exists("edits.log"):
                open("edits.log", "w")
            open("edits.log", "a").write(actual_file_path + "\n")
            open(actual_file_path, "w").write(await editor.getValue())
            window.hash.notify()

    async def create_file():
        new_file_path = os.path.join(BASE_PATH, new_file_name_input())
        try:
            if os.path.exists(new_file_path) and not is_writable_file(new_file_path):
                raise Exception(f"{new_file_path} is not writable")
            open(new_file_path, "w").write(await editor.getValue())
            main = render_utils.get_module_name(new_file_path)
            if args:
                main = f"{main}#{args}"
            window.hash.set(json.dumps())
            window.location_reload()
        except OSError as e:
            antd.Modal.error(
                {"content": f"Failed to create {new_file_path}. {e.args[1]}."}
            )
        except Exception as e:
            antd.Modal.error({"content": f"Failed to create {new_file_path}. {e}."})

    return html.div(
        [
            html.div(
                [
                    antd.Button(
                        ant_icons.CaretRightFilled(),
                        type="primary",
                        onClick=reload,
                        style={"margin": 10},
                    ),
                    antd.Modal(
                        [new_file_name_input],
                        title="Enter a file name",
                        open=create_file_visible,
                        onOk=create_file,
                        onCancel=lambda: create_file_visible.set(False),
                    ),
                    antd.Button(
                        ant_icons.FolderOpenFilled(),
                        type="primary",
                        onClick=show_file_selection_window,
                    ),
                    file_selection_window,
                ]
            ),
            dock_layout,
        ]
    )
