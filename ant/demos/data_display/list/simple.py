import render as r
import render_antd as antd
import render_html as html

data = [
    "Magna officia mollit commodo occaecat esse id.",
    "Ea nostrud aliqua duis tempor duis in dolor.",
    "Pariatur reprehenderit enim nulla sit ex adipiscing.",
    "Excepteur velit pariatur ad dolore ipsum ea.",
]


list_item_renderer_highlight = r.js_arrow(
    "list_item_renderer_highlight",
    "item => get_component('antd', 'List.Item')([get_component('antd', 'Typography.Text')([item], { mark: true })])",
)

list_item_renderer = r.js_arrow(
    "list_item_renderer", "get_component('antd', 'List.Item')"
)


def app(_):
    return html.div(
        [
            antd.Divider("Default Size", orientation="left"),
            antd.List(
                header=html.div("Header"),
                footer=html.div("Footer"),
                bordered=True,
                dataSource=data,
                renderItem=list_item_renderer_highlight,
            ),
            antd.Divider("Small Size", orientation="left"),
            antd.List(
                size="small",
                header=html.div("Header"),
                footer=html.div("Footer"),
                bordered=True,
                dataSource=data,
                renderItem=list_item_renderer,
            ),
            antd.Divider("Large Size", orientation="left"),
            antd.List(
                size="large",
                header=html.div("Header"),
                footer=html.div("Footer"),
                bordered=True,
                dataSource=data,
                renderItem=list_item_renderer,
            ),
        ]
    )
