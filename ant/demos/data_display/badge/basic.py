import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Badge(html.a(href="#", className="head-example"), count=5),
            antd.Badge(
                html.a(href="#", className="head-example"), count=0, showZero=True
            ),
            antd.Badge(
                html.a(href="#", className="head-example"),
                count=ant_icons.ClockCircleOutlined(style={"color": "#f5222d"}),
            ),
        ]
    )
