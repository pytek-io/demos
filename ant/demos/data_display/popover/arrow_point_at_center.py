import render_antd as antd
import render_html as html


def app():
    content = html.div([html.p("Content"), html.p("Content")])
    text = html.span("Title")
    return html.div(
        [
            antd.Popover(
                antd.Button("Align edge"),
                placement="topLeft",
                title=text,
                content=content,
            ),
            antd.Popover(
                antd.Button("Arrow points to center"),
                placement="topLeft",
                title=text,
                content=content,
                arrowPointAtCenter=True,
            ),
        ]
    )
