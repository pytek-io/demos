import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def render_title(title):
    return html.span(
        [
            title,
            html.a(
                "more",
                style={"float": "right"},
                href="https://www.google.com/search?q=antd",
                target="_blank",
                rel="noopener noreferrer",
            ),
        ]
    )


def render_item(title: str, count: int):
    return {
        "value": title,
        "label": html.div(
            [title, html.span([ant_icons.UserOutlined(), count])],
            style={"display": "flex", "justifyContent": "space-between"},
        ),
    }


options = [
    {
        "label": render_title("Libraries"),
        "options": [
            render_item("AntDesign", 10000),
            render_item("AntDesign UI", 10600),
        ],
    },
    {
        "label": render_title("Solutions"),
        "options": [
            render_item("AntDesign UI FAQ", 60100),
            render_item("AntDesign FAQ", 30010),
        ],
    },
    {
        "label": render_title("Articles"),
        "options": [render_item("AntDesign design language", 100000)],
    },
]


def app(_):
    return antd.AutoComplete(
        antd.Input.Search(size="large", placeholder="input here"),
        dropdownMatchSelectWidth=500,
        style={"width": 250},
        options=options,
    )
