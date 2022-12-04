import reflect as r
import reflect_antd as antd
import reflect_html as html

columns = [
    {
        "title": "Name",
        "dataIndex": "name",
        "key": "name",
        "width": 150,
        "render": r.js("a"),
    },
    {"title": "Age", "dataIndex": "age", "key": "age", "width": 80},
    {"title": "Address", "dataIndex": "address", "key": "address 1", "ellipsis": True},
    {
        "title": "Long Column Long Column Long Column",
        "dataIndex": "address",
        "key": "address 2",
        "ellipsis": True,
    },
    {
        "title": "Long Column Long Column",
        "dataIndex": "address",
        "key": "address 3",
        "ellipsis": True,
    },
    {
        "title": "Long Column",
        "dataIndex": "address",
        "key": "address 4",
        "ellipsis": True,
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


def app():
    return antd.Table(columns=columns, dataSource=data)
