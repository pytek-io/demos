from render_html import *
from render_antd import Input, Tooltip
from render_ant_icons import InfoCircleOutlined, UserOutlined
def app():
    return[
 Input(InfoCircleOutlined(style=dict(color='rgba(0)), placeholder="Enter your username", prefix="{UserOutlined(className=", site-form-item-icon")}"=True, suffix="{         <Tooltip title=", Extra=True, information"=True),
 br(),
 br(),
 Input(prefix="￥", suffix="RMB"),
 br(),
 br(),
 Input(prefix="￥", suffix="RMB", disabled=True),
]