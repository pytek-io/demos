"""
    Simple todo application inspired from https://github.com/leonardopliski/react-antd-todo
"""
import json
import os
import pathlib

import render as r
import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html
from more_itertools import ilen

FIRST_COL_BREAK_POINTS = {"xs": 24, "sm": 24, "md": 17, "lg": 19, "xl": 20}
SECOND_COL_BREAK_POINTS = {"xs": 24, "sm": 24, "md": 7, "lg": 5, "xl": 4}
DEFAULT_FILE_NAME = "default_todo_list.json"


def save_to_file(file, data):
    pathlib.Path(file).write_text(json.dumps(data))


def load_from_file(file):
    return json.loads(pathlib.Path(file).read_text())


class App:
    def __init__(self, window: r.Window):
        if not window.hash():
            window.hash.set("default_todo_list")
        self.items_obs_actual = r.ObservableList([], key="items_obs")
        self.items_obs = r.Mapping(
            r.DictOfObservables, self.items_obs_actual, key="items_obs"
        )
        self.actual_items = []
        self.description = antd.Input(
            placeholder="What needs to be done?",
            onPressEnter=self.add_new_item,
            key="self.description",
        )

        def on_file_name_update():
            self.file_name = window.hash() or "default_todo_list"
            if not self.file_name.endswith(".json"):
                self.file_name += ".json"
            file_path = pathlib.Path(os.getcwd(), self.file_name)
            if file_path.exists():
                self.actual_items, self.todo_item_counter = load_from_file(file_path)
            else:
                self.actual_items, self.todo_item_counter = [], 0
            self.items_obs_actual.set(self.actual_items)

        def on_list_update():
            nb_completed = ilen(
                None for item_obs in self.items_obs if item_obs["completed"]
            )
            window.update_title(
                f"({nb_completed}/{len(self.items_obs)}) {self.file_name}"
            )
            print("Saving to file", self.actual_items, self.todo_item_counter)
            save_to_file(self.file_name, (self.actual_items, self.todo_item_counter))

        r.autorun(on_file_name_update, "on_save_file_update")
        r.autorun(on_list_update, "on_list_update")

    def create_todo_item_row(self, item_obs: r.DictOfObservables):
        return antd.List.Item(
            html.div(
                antd.Tag(
                    item_obs["description"],
                    color=lambda: "cyan" if item_obs["completed"]() else "red",
                )
            ),
            actions=[
                antd.Popconfirm(
                    antd.Button("X", type="primary", danger=True),
                    title="Are you sure you want to delete this item?",
                    onConfirm=lambda: self.items_obs_actual.remove(
                        item_obs.back_reference()
                    ),
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
            key=item_obs["key"](),
        )

    def add_new_item(self):
        if self.description():
            self.items_obs_actual.append(
                {
                    "description": self.description(),
                    "completed": False,
                    "key": self.todo_item_counter,
                }
            )
            self.description.set("")
            self.todo_item_counter += 1

    def content(self):
        top_row = antd.Row(
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
            key="top_row",
            gutter=20,
        )
        form = antd.Card(top_row, title="Create a new todo")
        todo_list = antd.Card(
            antd.List(
                r.Mapping(
                    self.create_todo_item_row, self.items_obs, key="todo_item_rows"
                ),
                locale={"emptyText": "Nothing to do."},
            ),
            title="Items",
        )
        return antd.Row(
            antd.Col(
                [form, todo_list],
                style={"padding": 20, "maxWidth": 800, "width": "100%"},
            ),
            justify="center",
        )
