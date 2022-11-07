import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Button("Primary", type="primary", block=True),
            antd.Button("Default", block=True),
            antd.Button("Dashed", type="dashed", block=True),
            antd.Button("Link", type="link", block=True),
        ]
    )
