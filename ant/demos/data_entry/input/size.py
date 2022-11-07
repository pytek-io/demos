from reflect_html import *
from reflect_antd import Input
from reflect_ant_icons import UserOutlined


def app():
    return div([
        Input(size="large", placeholder="large size", prefix=UserOutlined([])),
        br(),
        br(),
        Input(placeholder="default size", prefix=UserOutlined([])),
        br(),
        br(),
        Input(size="small", placeholder="small size", prefix=UserOutlined([])),
    ]
)