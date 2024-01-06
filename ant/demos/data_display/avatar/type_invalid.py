from render_html import *
from render_antd import Avatar, Image
from render_ant_icons import UserOutlined
def app():
    return[
 Avatar(icon=UserOutlined([])),
 Avatar("U"),
 Avatar("USER", size=40),
 Avatar(src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"),
 Avatar(src="{Image(src=", https:=True, zos.alipayobjects.com=True, rmsportal=True, ODTLcjxAfvqbxHnVXCYX.png")}"=True),
 Avatar("U", style=dict(color='#f56a00', backgroundColor='#fde3cf')),
 Avatar(style=dict(backgroundColor='#87d068'), icon=UserOutlined([])),
]