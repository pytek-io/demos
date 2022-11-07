import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Divider(style=dict(borderWidth=2, borderColor="#7cb305")),
            antd.Divider(style=dict(borderColor="#7cb305"), dashed=True),
            antd.Divider("Text", style=dict(borderColor="#7cb305"), dashed=True),
            antd.Divider(type="vertical", style=dict(height=60, borderColor="#7cb305")),
            antd.Divider(
                type="vertical",
                style=dict(height=60, borderColor="#7cb305"),
                dashed=True,
            ),
        ]
    )
