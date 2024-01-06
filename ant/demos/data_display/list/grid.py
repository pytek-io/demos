import render_html as html
import render_antd as antd
import render as r


def app():
    data = [
        {"title": "Title 1"},
        {"title": "Title 2"},
        {"title": "Title 3"},
        {"title": "Title 4"},
    ]
    return antd.List(
        "Card content",
        grid=dict(gutter=16, column=4),
        dataSource=data,
        renderItem= r.js_arrow("formatter", "item => render_ant.List.Item(render_ant.Card(null, item))")
    )
