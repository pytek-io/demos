import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Button("Primary", type="primary", block=True),
            antd.Button("Default", block=True),
            antd.Button("Dashed", type="dashed", block=True),
            antd.Button("Link", type="link", block=True),
        ]
    )
