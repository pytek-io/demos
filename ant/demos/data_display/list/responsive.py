import render as r
import render_antd as antd

renderer = """item => (
    get_component('antd', 'List.Item')(
        get_component('antd', 'Card')("Card content", { title: item.title })
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


def app(_):
    return antd.List(
        grid=dict(gutter=16, xs=1, sm=2, md=4, lg=4, xl=6, xxl=3),
        dataSource=data,
        renderItem=r.js_arrow("render_item", renderer),
    )
