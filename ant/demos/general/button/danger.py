import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Button("Primary", type="primary", danger=True),
            antd.Button("Default", danger=True),
            antd.Button("Dashed", type="dashed", danger=True),
            antd.Button("Text", type="text", danger=True),
            antd.Button("Link", type="link", danger=True),
        ]
    )
