"""
    Simple todo application based on https://github.com/leonardopliski/react-antd-todo
"""
import json
from os.path import split, join, dirname
from itertools import count

from reflect import Mapping, autorun, get_window, make_observable
from reflect_ant_icons import (
    CaretDownFilled,
    CaretUpFilled,
    CheckOutlined,
    CloseOutlined,
    PlusCircleFilled,
)
from reflect_antd import (
    Button,
    Card,
    Col,
    Input,
    List,
    PageHeader,
    Popconfirm,
    Row,
    Switch,
    Tag,
    Tooltip,
)
from reflect_html import div

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
    open(file, "w").write(json.dumps(data))


def load_from_file(file):
    return json.loads(open(file, "r").read())


class Application:
    def __init__(self, file_path, update_title):
        initial_items = load_from_file(file_path)
        file_name = split(file_path)[1].split(".")[0]
        self.todo_item_counter = count(
            (max(item["key"] for item in initial_items) + 1) if initial_items else 0
        )
        self.items = make_observable(initial_items, depth=3, key="self.todos")
        self.todo_item_rows = Mapping(
            self.create_todo_item_row,
            self.items,
            key="self.todo_items",
        )

        def on_change():
            nb_completed = iterable_length(
                filter(lambda item: item["completed"](), self.items())
            )
            update_title(f"({nb_completed}/{len(self.items())}) {file_name}")
            save_to_file(file_path, initial_items)

        autorun(on_change)
        self.description = Input(
            placeholder="What needs to be done?",
            onPressEnter=self.add_new_item,
            key="self.description",
        )
        self.top_row = Row(
            [
                Col(
                    [self.description],
                    key="col1",
                    **FIRST_COL_BREAK_POINTS,
                ),
                Col(
                    Button(
                        [PlusCircleFilled(), "Add todo"],
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

    def move_item(self, key, up_or_down):
        self.items.move(
            find_index(self.items(), lambda v: v["key"]() == key),
            1 if up_or_down else -1,
        )

    def create_todo_item_row(self, item):
        key = item["key"]()
        return List.Item(
            div(
                Tag(
                    item["description"],
                    color=lambda: "cyan" if item["completed"]() else "red",
                    className="todo-tag",
                ),
                className="todo-item",
            ),
            actions=[
                Button(CaretUpFilled(), onClick=lambda: self.move_item(key, False)),
                Button(CaretDownFilled(), onClick=lambda: self.move_item(key, True)),
                Popconfirm(
                    Button(
                        "X", className="remove-todo-button", type="primary", danger=True
                    ),
                    title="Are you sure you want to delete this item?",
                    onConfirm=lambda: self.items.remove(item),
                ),
                Tooltip(
                    Switch(
                        checkedChildren=CheckOutlined(),
                        unCheckedChildren=CloseOutlined(),
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
                dict(
                    description=self.description(),
                    completed=False,
                    key=next(self.todo_item_counter),
                )
            )
            self.description.set("")

    def root(self):
        title = PageHeader(
            title="Add Todo",
            subTitle="To add a todo, just fill the form below and click in add todo or press enter.",
        )
        form = Card(
            self.top_row,
            title="Create a new todo",
        )
        todo_list = Card(
            List(
                # the div is added as for some reasons ant List does not key its immedidate child (meaning the whole tree is rerenderd when the content is updated)
                div(self.todo_item_rows),
                locale={"emptyText": "Nothing to do."},
            ),
            title="Items",
        )
        components = [
            Row(
                Col(component, span=24),
                style={"paddingTop": 20},
            )
            for component in [title, form, todo_list]
        ]
        return Col(
            components,
            style={"paddingLeft": 20, "paddingRight": 20},
            className="todos-container",
        )


def app():
    window = get_window()

    return div(
        lambda: Application(
            window.hash() or join(dirname(__file__), "default_todo_list.json"),
            window.update_title,
        ).root()
    )
