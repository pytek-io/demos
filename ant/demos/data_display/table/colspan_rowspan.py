import reflect as r
import reflect_antd as antd
import reflect_html as html

data = [
    {
        "key": "1",
        "name": "John Brown",
        "age": 32,
        "tel": "0571-22098909",
        "phone": 18889898989,
        "address": "New York No. 1 Lake Park",
    },
    {
        "key": "2",
        "name": "Jim Green",
        "tel": "0571-22098333",
        "phone": 18889898888,
        "age": 42,
        "address": "London No. 1 Lake Park",
    },
    {
        "key": "3",
        "name": "Joe Black",
        "age": 32,
        "tel": "0575-22098909",
        "phone": 18900010002,
        "address": "Sidney No. 1 Lake Park",
    },
    {
        "key": "4",
        "name": "Jim Red",
        "age": 18,
        "tel": "0575-22098909",
        "phone": 18900010002,
        "address": "London No. 2 Lake Park",
    },
    {
        "key": "5",
        "name": "Jake White",
        "age": 18,
        "tel": "0575-22098909",
        "phone": 18900010002,
        "address": "Dublin No. 2 Lake Park",
    },
]
render = r.js("merge_col", 4)
columns = [
    {"title": "Name", "dataIndex": "name", "render": r.js("render_name")},
    {"title": "Age", "dataIndex": "age", "render": render},
    {
        "title": "Home phone",
        "colSpan": 2,
        "dataIndex": "tel",
        "render": r.js("render_home_phone", 4),
    },
    {"title": "Phone", "colSpan": 0, "dataIndex": "phone", "render": render},
    {"title": "Address", "dataIndex": "address", "render": render},
]


def app():
    return antd.Table(columns=columns, dataSource=data, bordered=True)
