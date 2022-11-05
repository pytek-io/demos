"""
    Simple todo application based on https://github.com/leonardopliski/react-antd-todo
"""
import json
import os

import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

import reflect as r

CSS = ["demos/todo_list.css"]
FIRST_COL_BREAK_POINTS = dict(xs=24, sm=24, md=17, lg=19, xl=20)
SECOND_COL_BREAK_POINTS = dict(xs=24, sm=24, md=7, lg=5, xl=4)
DEFAULT_FILE_NAME = "default_todo_list.json"


def find_index(values, match):
    for index, value in enumerate(values):
        if match(value):
            return index


def iterable_length(iterable):
    return sum(1 for _ in iterable)


def save_to_file(file, data):
    content = json.dumps(data)
    open(file, "w").write(content)


def load_from_file(file):
    try:
        return json.loads(open(file, "r").read())
    except Exception as e:
        raise Exception(f"Failed to read {file}. {e}") from e


class Application:
    def __init__(self, file_path, update_title):
        if not "." in os.path.basename(file_path):
            file_path += ".json"
        file_path = os.path.join(os.path.split(__file__)[0], file_path)
        if os.path.exists(file_path):
            items, self.todo_item_counter = load_from_file(file_path)
        else:
            items, self.todo_item_counter = [], 0
        file_name = os.path.basename(file_path).split(".")[0]
        self.items = r.create_observable(items, depth=3)
        self.todo_item_rows = r.create_mapping(
            self.create_todo_item_row,
            self.items,
            key="self.todo_items",
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

        def on_change():
            nb_completed = iterable_length(
                filter(lambda item: item["completed"](), self.items.observables())
            )
            update_title(
                f"({nb_completed}/{len(self.items.observables())}) {file_name}"
            )

        r.autorun(on_change)

    def move_item(self, key, up_or_down):
        self.items.move(
            find_index(self.items(), lambda v: v["key"] == key), 1 if up_or_down else -1
        )

    def create_todo_item_row(self, item):
        key = item["key"]()
        return antd.List.Item(
            html.div(
                antd.Tag(
                    item["description"],
                    color=lambda: "cyan" if item["completed"]() else "red",
                    className="todo-tag",
                ),
                className="todo-item",
            ),
            actions=[
                antd.Button(
                    ant_icons.CaretUpFilled(),
                    onClick=lambda: self.move_item(key, False),
                ),
                antd.Button(
                    ant_icons.CaretDownFilled(),
                    onClick=lambda: self.move_item(key, True),
                ),
                antd.Popconfirm(
                    antd.Button(
                        "X", className="remove-todo-button", type="primary", danger=True
                    ),
                    title="Are you sure you want to delete this item?",
                    onConfirm=lambda: self.items.remove(item),
                ),
                antd.Tooltip(
                    antd.Switch(
                        checkedChildren=ant_icons.CheckOutlined(),
                        unCheckedChildren=ant_icons.CloseOutlined(),
                        checked=item["completed"],
                    ),
                    title=lambda: "Mark as uncomplete"
                    if item["completed"]()
                    else "Mark as completed",
                ),
            ],
            className="list-item",
            key=key,
        )

    def add_new_item(self):
        if self.description():
            self.items.append(
                {
                    "description": self.description(),
                    "completed": False,
                    "key": self.todo_item_counter,
                }
            )
            self.description.set("")
            self.todo_item_counter += 1

    def root(self):
        title = antd.PageHeader(
            title="Add Todo",
            subTitle="To add a todo, just fill the form below and click in add todo or press enter.",
        )
        form = antd.Card(self.top_row, title="Create a new todo")
        todo_list = antd.Card(
            antd.List(
                html.div(self.todo_item_rows), locale={"emptyText": "Nothing to do."}
            ),
            title="Items",
        )
        components = [
            antd.Row(antd.Col(component, span=24), style={"paddingTop": 20})
            for component in [title, form, todo_list]
        ]
        return antd.Col(
            components,
            style={"paddingLeft": 20, "paddingRight": 20},
            className="todos-container",
        )


def app():
    window = r.get_window()
    return html.div(
        lambda: Application(
            window.hash()
            or os.path.join(os.path.dirname(__file__), "default_todo_list.json"),
            window.update_title,
        ).root()
    )
