import reflect as r
import reflect_antd as antd


renderer = """item => (
    reflect_ant.List.Item(
        reflect_ant.Card("Card content", { title: item.title })
    )
)"""

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


def app():
    return antd.List(
        grid=dict(gutter=16, xs=1, sm=2, md=4, lg=4, xl=6, xxl=3),
        dataSource=data,
        renderItem=r.js_arrow("render_item", renderer),
    )
