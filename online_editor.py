import json
import os

from reflect import get_window, make_observable
from reflect.utils import CatchError, decode_url, is_writable_file
from reflect_ant_icons import CaretRightFilled, FolderOpenFilled
from reflect_antd import Button, Input, Modal
from reflect_html import div, section
from reflect_rcdock import DockLayout
from reflect_utils.common import (
    create_file_chooser,
    create_tab_inserter,
    evaluate_demo_module,
)
from reflect_utils.misc import get_module_name
from reflect_utils.md_parsing import (
    extract_file_path_and_language,
    monaco_language_from_extension,
    parse_md_doc,
)

from demos.ant.main import create_code_editor

TITLE = "Online Editor"
BASE_PATH = "demos"


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


def app():
    window = get_window()
    arguments = json.loads(window.hash()) if window.hash() else {"main": "hello_world.py"}
    main, css = arguments["main"], arguments.get("css", [])
    window.add_css(css)
    main, kwargs = decode_url(main)
    counter = 0
    # this is taken from dock_manager demo (should be factored out)
    def create_tab(title, application):
        nonlocal counter
        counter += 1
        return {
            "id": str(counter),
            "title": title,
            "content": application,
            "cached": True,
        }

    actual_file_path, language = extract_file_path_and_language(main)
    editor = create_editor(actual_file_path, language, read_only=False)

    def delayed_component():
        window.hash()
        if language == "python":
            _success, css, title, component = evaluate_demo_module(main, kwargs)
            if css:
                window.add_css(css)
            component = section(
                component, id="code-box-demo", className="code-box-demo"
            )
        else:
            component = parse_md_doc(open(actual_file_path).read())
        return component

    title = "Preview"
    _, file_name = os.path.split(actual_file_path)
    defaultLayout = {
        "dockbox": {
            "mode": "vertical",
            "children": [
                {
                    "tabs": [
                        create_tab(
                            file_name,
                            editor,
                        ),
                    ],
                },
                {
                    "tabs": [
                        create_tab(
                            title or file_name.split(".")[0],
                            div(
                                delayed_component,
                                style={
                                    "padding": 20,
                                    "overflow": "scroll",
                                    "height": "inherit",
                                },
                            ),
                        )
                    ],
                },
            ],
        }
    }
    dock_layout = DockLayout(
        defaultLayout=defaultLayout,
        style={
            "position": "absolute",
            "left": 0,
            "top": 50,
            "right": 0,
            "bottom": 0,
        },
    )
    insert_tab = create_tab_inserter(dock_layout)
    create_file_visible = make_observable(False, key="create_file_visible")

    async def open_file(file):
        if file:
            file = os.path.join(BASE_PATH, file)
            _folder_path, file_name = os.path.split(file)
            editor = create_editor(
                file, monaco_language_from_extension(file_name), read_only=True
            )
            await insert_tab(file_name, editor)

    file_selection_window, show_file_selection_window = create_file_chooser(
        BASE_PATH, title="Select file to open", on_ok=open_file
    )

    name, extension = file_name.rsplit(".", 1)
    default_new_file_name = f"{name}_test.{extension}"
    new_file_name_input = Input(defaultValue=default_new_file_name)

    async def reload():
        if not is_writable_file(actual_file_path):
            create_file_visible.set(True)
        else:
            if not os.path.exists("edits.log"):
                open("edits.log", "w")
            open("edits.log", "a").write(actual_file_path + "\n")
            open(actual_file_path, "w").write(await editor.getValue())
            window.hash.touch()

    async def create_file():
        with CatchError():
            new_file_path = os.path.join(BASE_PATH, new_file_name_input())
            try:
                if os.path.exists(new_file_path) and not is_writable_file(
                    new_file_path
                ):
                    raise Exception(f"{new_file_path} is not writable")
                open(new_file_path, "w").write(await editor.getValue())
                main = get_module_name(new_file_path)
                dict(main=main, css=css)
                if args:
                    main = f"{main}#{args}"
                window.hash.set(json.dumps())
                window.location_reload()
            except OSError as e:
                Modal.error(
                    {"content": f"Failed to create {new_file_path}. {e.args[1]}."}
                )
            except Exception as e:
                Modal.error({"content": f"Failed to create {new_file_path}. {e}."})

    return div(
        [
            div(
                [
                    Button(
                        CaretRightFilled(),
                        type="primary",
                        onClick=reload,
                        style=dict(margin=10),
                    ),
                    Modal(
                        [new_file_name_input],
                        title="Enter a file name",
                        visible=create_file_visible,
                        onOk=create_file,
                        onCancel=lambda: create_file_visible.set(False),
                        closable=True,
                    ),
                    Button(
                        FolderOpenFilled(),
                        type="primary",
                        onClick=show_file_selection_window,
                    ),
                    file_selection_window,
                ]
            ),
            dock_layout,
        ]
    )
