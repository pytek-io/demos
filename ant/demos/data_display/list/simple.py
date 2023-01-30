import reflect as r
import reflect_antd as antd
import reflect_html as html

data = [
    "Magna officia mollit commodo occaecat esse id.",
    "Ea nostrud aliqua duis tempor duis in dolor.",
    "Pariatur reprehenderit enim nulla sit ex adipiscing.",
    "Excepteur velit pariatur ad dolore ipsum ea.",
]


list_item_renderer_highlight = r.JSMethod(
    "list_item_renderer_highlight",
    """
return createElement(
  reflect_ant.List.Item,
  {},
  createElement(reflect_ant.Typography.Text, { mark: true }, item)
);
""",
    "item",
)

list_item_renderer = r.JSMethod(
    "list_item_renderer",
    """return createElement(reflect_ant.List.Item, {}, item);""",
    "item",
)


def app():
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
