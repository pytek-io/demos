from reflect_html import *
from reflect_antd import Table
from reflect import Callback
from reflect import make_observable

columns = [
    {
        "title": "Name",
        "dataIndex": "name",
    },
    {
        "title": "Age",
        "dataIndex": "age",
    },
    {
        "title": "Address",
        "dataIndex": "address",
    },
]

data = [
    {
        "key": i,
        "name": f"Edward {i}",
        "age": 32,
        "address": f"London Park no. {i}",
    }
    for i in range(46)
]


def selectedRowKeys(keys):
    print("selected", keys)


def app():
    raise Exception("this is crashing badly!")
    selectedRowKeys = make_observable([])

    def onChange(newSelectedRowKeys):
        print(
            f"selectedRowKeys: {newSelectedRowKeys}"
        )  # , "selectedRows: ", selectedRows)
        selectedRowKeys.set(newSelectedRowKeys)

    def select_keys(selector):
        return Callback(
            lambda selectable_keys: selectedRowKeys.set(
                [key for key in selectable_keys if selector(key)]
            )
        )

    rowSelection = {
        # "selectedRowKeys": selectedRowKeys,
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
    # rowSelection=rowSelection, 
    return Table(columns=columns, dataSource=data)
