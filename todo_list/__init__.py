"""
    Simple todo application based on https://github.com/leonardopliski/react-antd-todo
"""
import os
import json
import pathlib

import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

import reflect as r
from typing import Dict, Any

CSS = ["demos/todo_list.css"]
FIRST_COL_BREAK_POINTS = dict(xs=24, sm=24, md=17, lg=19, xl=20)
SECOND_COL_BREAK_POINTS = dict(xs=24, sm=24, md=7, lg=5, xl=4)
DEFAULT_FILE_NAME = "default_todo_list.json"


def iterable_length(iterable):
    return sum(1 for _ in iterable)


def save_to_file(file, data):
    pathlib.Path(file).write_text(json.dumps(data))


def load_from_file(file):
    try:
        return json.loads(pathlib.Path(file).read_text())
    except Exception as e:
        raise Exception(f"Failed to read {file}. {e}") from e


class Application:
    def __init__(self, file_path, update_title):
        file_path = pathlib.Path(os.getcwd(), file_path)
        if not "." in file_path.name:
            file_path = file_path.with_name(file_path.name + ".json")
        if file_path.exists():
            self.items, self.todo_item_counter = load_from_file(file_path)
        else:
            self.items, self.todo_item_counter = [], 0
        self.items_obs = r.ObservableList(self.items, key="self.items_obs")
        self.todo_item_rows = r.Mapping(
            self.create_todo_item_row,
            self.items_obs,
            key="self.todo_item_rows",
            evaluate_argument=False,
        )
        self.description = antd.Input(
            placeholder="What needs to be done?",
            onPressEnter=self.add_new_item,
            key="self.description",
        )
        self.top_row = antd.Row(
            [
                antd.Col([self.description], key="col1", **FIRST_COL_BREAK_POINTS),
                antd.Col(
                    antd.Button(
                        [ant_icons.PlusCircleFilled(), "Add todo"],
                        type="primary",
                        onClick=self.add_new_item,
                        block=True,
                    ),
                    key="col2",
                    **SECOND_COL_BREAK_POINTS,
                ),
            ],
            key="row1",
            gutter=20,
        )
        file_name = file_path.name.split(".", 1)[0]

        def on_change():
            nb_completed = iterable_length(
                filter(lambda item: item["completed"], self.items_obs)
            )
            update_title(f"({nb_completed}/{len(self.items_obs)}) {file_name}")
            save_to_file(file_path, (self.items, self.todo_item_counter))

        r.autorun(on_change)

    def create_todo_item_row(self, item: Dict[str, Any]):
        item_obs = r.DictOfObservables(item)
        key = item_obs["key"]()
        return antd.List.Item(
            html.div(
                antd.Tag(
                    item_obs["description"],
                    color=lambda: "cyan" if item_obs["completed"]() else "red",
                    className="todo-tag",
                ),
                className="todo-item",
            ),
            actions=[
                antd.Popconfirm(
                    antd.Button(
                        "X", className="remove-todo-button", type="primary", danger=True
                    ),
                    title="Are you sure you want to delete this item?",
                    onConfirm=lambda: self.items_obs.remove(item),
                ),
                antd.Tooltip(
                    antd.Switch(
                        checkedChildren=ant_icons.CheckOutlined(),
                        unCheckedChildren=ant_icons.CloseOutlined(),
                        checked=item_obs["completed"],
                        style={"width": 30},
                    ),
                    title=lambda: "Mark as uncomplete"
                    if item_obs["completed"]()
                    else "Mark as completed",
                ),
            ],
            className="list-item",
            key=key,
        )

    def add_new_item(self):
        if self.description():
            self.items_obs.append(
                {
                    "description": self.description(),
                    "completed": False,
                    "key": self.todo_item_counter,
                }
            )
            self.description.set("")
            self.todo_item_counter += 1

    def root(self):
        # title = antd.LayoutHeader(
        #     title="Add Todo",
        #     subTitle="To add a todo, just fill the form below and click in add todo or press enter.",
        # )
        form = antd.Card(self.top_row, title="Create a new todo")
        todo_list = antd.Card(
            antd.List(
                html.div(self.todo_item_rows), locale={"emptyText": "Nothing to do."}
            ),
            title="Items",
        )
        components = [
            antd.Row(antd.Col(component, span=24), style={"paddingTop": 20})
            for component in [form, todo_list]
        ]
        return antd.Col(
            components,
            style={"paddingLeft": 20, "paddingRight": 20},
            className="todos-container",
        )


def app(window: r.Window):
    # rmk: we define the whole content as a hash dependency
    return html.div(
        lambda: Application(
            window.hash() or "default_todo_list",
            window.update_title,
        ).root()
    )
