import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Avatar(
        size=dict(xs=24, sm=32, md=40, lg=64, xl=80, xxl=100),
        icon=ant_icons.AntDesignOutlined([]),
    )
