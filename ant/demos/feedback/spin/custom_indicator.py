import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app():
    return antd.Spin(indicator=ant_icons.LoadingOutlined(style={"fontSize": 24}))
