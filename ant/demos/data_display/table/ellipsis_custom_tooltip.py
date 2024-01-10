import render as r
import render_antd as antd

create_anchor = r.js_arrow("create_anchor", "text => render_html.a(text)")

address_renderer = r.js_arrow(
    "address_renderer",
    "address => render_ant.Tooltip(address, {placement: 'topLeft', title: address})",
)


columns = [
    {
        "title": "Name",
        "dataIndex": "name",
        "key": "name",
        "width": 150,
        "render": create_anchor,
    },
    {"title": "Age", "dataIndex": "age", "key": "age", "width": 80},
    {
        "title": "Address",
        "dataIndex": "address",
        "width": 80,
        "key": "address 1",
        "ellipsis": {"showTitle": False},
        "render": address_renderer,
    },
    {
        "title": "Long Column Long Column Long Column",
        "dataIndex": "address",
        "key": "address 2",
        "ellipsis": {"showTitle": False},
        "render": address_renderer,
    },
    {
        "title": "Long Column Long Column",
        "dataIndex": "address",
        "key": "address 3",
        "ellipsis": {"showTitle": False},
        "render": address_renderer,
    },
    {
        "title": "Long Column",
        "dataIndex": "address",
        "key": "address 4",
        "ellipsis": {"showTitle": False},
        "render": address_renderer,
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


def app(_):
    return antd.Table(columns=columns, dataSource=data)
