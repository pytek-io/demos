import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Badge(html.a(href="#", className="head-example"), count=5),
            antd.Badge(
                html.a(href="#", className="head-example"), count=0, showZero=True
            ),
            antd.Badge(
                html.a(href="#", className="head-example"),
                count=ant_icons.ClockCircleOutlined(style=dict(color="#f5222d")),
            ),
        ]
    )
