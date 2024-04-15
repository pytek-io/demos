import render_html as html
import render_ant_icons as ant_icons
import render_antd as antd

def app(_):
    return antd.Button(icon=ant_icons.MinusOutlined())
