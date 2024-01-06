import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Badge(ant_icons.NotificationOutlined(), dot=True),
            antd.Badge(ant_icons.NotificationOutlined(), count=0, dot=True),
            antd.Badge(html.a("Link something", href="#"), dot=True),
        ]
    )
