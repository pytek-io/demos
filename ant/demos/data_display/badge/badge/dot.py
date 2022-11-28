import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Badge(ant_icons.NotificationOutlined(), dot=True),
            antd.Badge(ant_icons.NotificationOutlined(), count=0, dot=True),
            antd.Badge(html.a("Link something", href="#"), dot=True),
        ]
    )
