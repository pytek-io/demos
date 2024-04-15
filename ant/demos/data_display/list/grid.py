import render as r
import render_antd as antd


def app(_):
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
        renderItem=r.js_arrow(
            "formatter",
            "item => render_antd', 'List.Item')([get_component('antd', 'Card')('Card Content', {title: item.title})])",
        ),
    )
