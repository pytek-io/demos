from reflect_html import *
from reflect_antd import List
from reflect import js


def app():
    raise NotImplementedError()
    data = [
        {
            "title": "Ant Design Title 1",
        },
        {
            "title": "Ant Design Title 2",
        },
        {
            "title": "Ant Design Title 3",
        },
        {
            "title": "Ant Design Title 4",
        },
    ]

    return List(
        itemLayout="horizontal",
        dataSource=data,
        renderItem=js("render_list_item"),
    )
