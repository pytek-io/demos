from reflect_antd import Table
from reflect import js


def app():
    columns = [
        {
            "title": "Name",
            "dataIndex": "name",
            "key": "name",
            # "render": js("a"),
        },
        {
            "title": "Age",
            "dataIndex": "age",
            "key": "age",
        },
        {
            "title": "Address",
            "dataIndex": "address",
            "key": "address",
        },
        {
            "title": "Tags",
            "key": "tags",
            "dataIndex": "tags",
            # "render": js("render_tags"),
        },
        {
            "title": "Action",
            "key": "action",
            # "render": js("render_action"),
        },
    ]

    data = [
        {
            "key": "1",
            "name": "John Brown",
            "age": 32,
            "address": "New York No. 1 Lake Park",
            "tags": ["nice", "developer"],
        },
        {
            "key": "2",
            "name": "Jim Green",
            "age": 42,
            "address": "London No. 1 Lake Park",
            "tags": ["winner"],
        },
        {
            "key": "3",
            "name": "Joe Black",
            "age": 32,
            "address": "Sidney No. 1 Lake Park",
            "tags": ["cool", "teacher"],
        },
    ]
    return Table(columns=columns, dataSource=data)
