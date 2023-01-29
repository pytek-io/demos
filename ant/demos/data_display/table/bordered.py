import reflect as r
import reflect_antd as antd

columns = [
    {"title": "Name", "dataIndex": "name"},
    {
        "title": "Cash Assets",
        "className": "column-money",
        "dataIndex": "money",
        "align": "right",
    },
    {"title": "Address", "dataIndex": "address"},
]
data = [
    {
        "key": "1",
        "name": "John Brown",
        "money": "￥300,000.00",
        "address": "New York No. 1 Lake Park",
    },
    {
        "key": "2",
        "name": "Jim Green",
        "money": "￥1,256,000.00",
        "address": "London No. 1 Lake Park",
    },
    {
        "key": "3",
        "name": "Joe Black",
        "money": "￥120,000.00",
        "address": "Sidney No. 1 Lake Park",
    },
]


def app():
    return antd.Table(
        columns=columns,
        dataSource=data,
        bordered=True,
    )
