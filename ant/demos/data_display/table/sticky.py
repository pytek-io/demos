from reflect_html import *
from reflect_antd import Table
from reflect import js


def app():
    columns = [
        {
            "title": "Full Name",
            "width": 100,
            "dataIndex": "name",
            "key": "name",
            "fixed": "left",
        },
        {
            "title": "Age",
            "width": 100,
            "dataIndex": "age",
            "key": "age",
            "fixed": "left",
        },
        {"title": "Column 1", "dataIndex": "address", "key": "1", "width": 150},
        {"title": "Column 2", "dataIndex": "address", "key": "2", "width": 150},
        {"title": "Column 3", "dataIndex": "address", "key": "3", "width": 150},
        {"title": "Column 4", "dataIndex": "address", "key": "4", "width": 150},
        {"title": "Column 5", "dataIndex": "address", "key": "5", "width": 150},
        {"title": "Column 6", "dataIndex": "address", "key": "6", "width": 150},
        {"title": "Column 7", "dataIndex": "address", "key": "7", "width": 150},
        {"title": "Column 8", "dataIndex": "address", "key": "8"},
        {
            "title": "Action",
            "key": "operation",
            "fixed": "right",
            "width": 100,
            "render": js("constant", a("action")),
        },
    ]
    data = [
        {
            "key": i,
            "name": f"Edward {i}",
            "age": 32,
            "address": f"London Park no. {i}",
        }
        for i in range(100)
    ]

    return Table(columns=columns, dataSource=data, scroll=dict(x=1500), sticky=True)
