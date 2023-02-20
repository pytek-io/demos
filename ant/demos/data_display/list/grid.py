import reflect_html as html
import reflect_antd as antd
import reflect as r


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
        renderItem= r.js_arrow("formatter", "item => reflect_ant.List.Item(reflect_ant.Card(null, {title:item.title}))")
    )
