import render_antd as antd
import render_html as html

content = html.div([html.p("Content"), html.p("Content")])


def app(_):
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
