import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app():
    return antd.Avatar(
        size={"xs": 24, "sm": 32, "md": 40, "lg": 64, "xl": 80, "xxl": 100},
        icon=ant_icons.AntDesignOutlined([]),
    )
