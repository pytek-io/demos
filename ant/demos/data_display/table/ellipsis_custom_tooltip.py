from reflect_html import *
from reflect_antd import Table, Tooltip
from reflect import js

columns = [
    {
        "title": "Name",
        "dataIndex": "name",
        "key": "name",
        "width": 150,
        "render": js("a"),
    },
    {"title": "Age", "dataIndex": "age", "key": "age", "width": 80},
    {
        "title": "Address",
        "dataIndex": "address",
        "key": "address 1",
        "ellipsis": {"showTitle": False},
        "render": js("render_address"),
    },
    {
        "title": "Long Column Long Column Long Column",
        "dataIndex": "address",
        "key": "address 2",
        "ellipsis": {"showTitle": False},
        "render": js("render_address"),
    },
    {
        "title": "Long Column Long Column",
        "dataIndex": "address",
        "key": "address 3",
        "ellipsis": {"showTitle": False},
        "render": js("render_address"),
    },
    {
        "title": "Long Column",
        "dataIndex": "address",
        "key": "address 4",
        "ellipsis": {"showTitle": False},
        "render": js("render_address"),
    },
]

data = [
    {
        "key": "1",
        "name": "John Brown",
        "age": 32,
        "address": "New York No. 1 Lake Park, New York No. 1 Lake Park",
    },
    {
        "key": "2",
        "name": "Jim Green",
        "age": 42,
        "address": "London No. 2 Lake Park, London No. 2 Lake Park",
    },
    {
        "key": "3",
        "name": "Joe Black",
        "age": 32,
        "address": "Sidney No. 1 Lake Park, Sidney No. 1 Lake Park",
    },
]


def app():
    return Table(columns=columns, dataSource=data)
