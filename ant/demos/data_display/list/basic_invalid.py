import render as r
import render_antd as antd


def app():
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

    render_item = """item => render_ant.List.Item(null,
    render_ant.List.Item.Meta(null, {
        avatar: render_ant.Avatar(null, { src: "https://joesch.moe/api/v1/random" }),
        title: render_html.a(item.title, { ref: "https://ant.design" }),
        description: "Ant Design, a design language for background applications, is refined by Ant UED Team",
    })
)"""

    return antd.List(
        itemLayout="horizontal",
        dataSource=data,
        renderItem=r.js_arrow("render_item", render_item)
    )
