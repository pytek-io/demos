from reflect_html import *
from reflect_antd import List
from reflect import js


def app():
    raise NotImplementedError()
    listData = [
        {
            "href": "https://ant.design",
            "title": f"ant design part {i}",
            "avatar": "https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png",
            "description": "Ant Design, a design language for background applications, is refined by Ant UED Team.",
            "content": "We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.",
        }
        for i in range(4)
    ]

    return List(
        itemLayout="vertical",
        dataSource=listData,
        footer=div(b("ant design"), "footer part"),
        renderItem=js("render_list_item1"),
    )
