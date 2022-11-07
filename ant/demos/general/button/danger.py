import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Button("Primary", type="primary", danger=True),
            antd.Button("Default", danger=True),
            antd.Button("Dashed", type="dashed", danger=True),
            antd.Button("Text", type="text", danger=True),
            antd.Button("Link", type="link", danger=True),
        ]
    )
