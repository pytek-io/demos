import render as r
import render_antd as antd


getCurrentAnchor = r.js_arrow(
    "getCurrentAnchor", "() => '#components-anchor-demo-static'"
)


def app():
    items = [
        {"href": "#components-anchor-demo-basic", "title": "Basic demo", "key": "1"},
        {"href": "#components-anchor-demo-static", "title": "Static demo", "key": "2"},
        {
            "children": [
                {"href": "#Anchor-Props", "title": "Anchor Props", "key": "3"},
                {"href": "#Link-Props", "title": "Link Props", "key": "4"},
            ],
            "href": "#API",
            "title": "API",
            "key": "5",
        },
    ]
    return antd.Anchor(items=items, affix=False, getCurrentAnchor=getCurrentAnchor)
