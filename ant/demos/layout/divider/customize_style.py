import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Divider(style={"borderWidth": 2, "borderColor": "#7cb305"}),
            antd.Divider(style={"borderColor": "#7cb305"}, dashed=True),
            antd.Divider("Text", style={"borderColor": "#7cb305"}, dashed=True),
            antd.Divider(
                type="vertical", style={"height": 60, "borderColor": "#7cb305"}
            ),
            antd.Divider(
                type="vertical",
                style={"height": 60, "borderColor": "#7cb305"},
                dashed=True,
            ),
        ]
    )
