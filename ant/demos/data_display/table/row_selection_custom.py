import reflect as r
from reflect import Callback
from reflect_antd import Table
from reflect_html import *

columns = [
    {"title": "Name", "dataIndex": "name"},
    {"title": "Age", "dataIndex": "age"},
    {"title": "Address", "dataIndex": "address"},
]
data = [
    {"key": i, "name": f"Edward {i}", "age": 32, "address": f"London Park no. {i}"}
    for i in range(46)
]


def selectedRowKeys(keys):
    print("selected", keys)


def app():
    selected_row_keys = r.ObservableList([])

    def onChange(newSelectedRowKeys):
        print(f"selectedRowKeys: {newSelectedRowKeys}")
        selected_row_keys.set(newSelectedRowKeys)

    def select_keys(selector):
        return Callback(
            lambda selectable_keys: selected_row_keys.set(
                [key for key in selectable_keys if selector(key)]
            )
        )

    def rowSelection():
        return {
            "selectedRowKeys": selected_row_keys(),
            "onChange": Callback(onChange),
            "selections": [
                Table.SELECTION_ALL,
                Table.SELECTION_INVERT,
                Table.SELECTION_NONE,
                {
                    "key": "odd",
                    "text": "Odd rows",
                    "onSelect": select_keys(lambda x: x % 2 == 1),
                },
                {
                    "key": "odd",
                    "text": "Even rows",
                    "onSelect": select_keys(lambda x: x % 2 == 0),
                },
            ],
        }

    return Table(columns=columns, rowSelection=rowSelection, dataSource=data)
