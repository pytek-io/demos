import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Divider(type="vertical"),
            html.a("Link", href="#"),
            antd.Divider(type="vertical"),
            html.a("Link", href="#"),
        ]
    )
