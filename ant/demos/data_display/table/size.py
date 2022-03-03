from reflect_html import *
from reflect_antd import Table

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
    {
        "title": "Tags",
        "dataIndex": "tags",
    },
]

data = [
    {
        "key": "1",
        "name": "John Brown",
        "age": 32,
        "address": "New York No. 1 Lake Park",
    },
    {
        "key": "2",
        "name": "Jim Green",
        "age": 42,
        "address": "London No. 1 Lake Park",
    },
    {
        "key": "3",
        "name": "Joe Black",
        "age": 32,
        "address": "Sidney No. 1 Lake Park",
    },
]

def app():
    return div(
        [
            h4("Middle size table"),
            Table(columns=columns, dataSource=data, size="middle"),
            h4("Small size table"),
            Table(columns=columns, dataSource=data, size="small"),
        ]
    )
