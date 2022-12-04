import reflect_antd as antd
import reflect_html as html

content = html.div([html.p("Content"), html.p("Content")])


def app():
    return html.div(
        [
            antd.Popover(
                antd.Button("Hover me"), content=content, title="Title", trigger="hover"
            ),
            antd.Popover(
                antd.Button("Focus me"), content=content, title="Title", trigger="focus"
            ),
            antd.Popover(
                antd.Button("Click me"), content=content, title="Title", trigger="click"
            ),
        ]
    )
