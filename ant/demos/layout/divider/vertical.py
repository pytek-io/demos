import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Divider(type="vertical"),
            html.a("Link", href="#"),
            antd.Divider(type="vertical"),
            html.a("Link", href="#"),
        ]
    )
