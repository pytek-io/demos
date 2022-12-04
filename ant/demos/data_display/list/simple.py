import reflect as r
import reflect_antd as antd
import reflect_html as html

data = [
    "Magna officia mollit commodo occaecat esse id.",
    "Ea nostrud aliqua duis tempor duis in dolor.",
    "Pariatur reprehenderit enim nulla sit ex adipiscing.",
    "Excepteur velit pariatur ad dolore ipsum ea.",
]


def app():
    return html.div(
        [
            antd.Divider("Default Size", orientation="left"),
            antd.List(
                header=html.div("Header"),
                footer=html.div("Footer"),
                bordered=True,
                dataSource=data,
                renderItem=r.js("simple_list_renderer_1"),
            ),
            antd.Divider("Small Size", orientation="left"),
            antd.List(
                size="small",
                header=html.div("Header"),
                footer=html.div("Footer"),
                bordered=True,
                dataSource=data,
                renderItem=r.js("simple_list_renderer_2"),
            ),
            antd.Divider("Large Size", orientation="left"),
            antd.List(
                size="large",
                header=html.div("Header"),
                footer=html.div("Footer"),
                bordered=True,
                dataSource=data,
                renderItem=r.js("simple_list_renderer_2"),
            ),
        ]
    )
