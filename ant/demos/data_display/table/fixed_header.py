from reflect_html import *
from reflect_antd import Table


columns = [
    {
        "title": "Name",
        "dataIndex": "name",
        "width": 150,
    },
    {
        "title": "Age",
        "dataIndex": "age",
        "width": 150,
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
    for i in range(100)
]


def app():
    return Table(
        columns=columns,
        dataSource=data,
        pagination=dict(pageSize=50),
        scroll=dict(y=240),
    )
