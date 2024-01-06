from render_html import *
from render_antd import Skeleton, Switch, Card, Avatar
from render_ant_icons import EditOutlined, EllipsisOutlined, SettingOutlined
Meta = Card.Meta
loading = this.loading
def app():
    return[
 Switch(checked=!loading, onChange=this.onChange),
 Card([Meta(avatar="{               <Avatar src=", https:=True, zos.alipayobjects.com=True, rmsportal=True, ODTLcjxAfvqbxHnVXCYX.png"=True), "}"             title="Card title"             description="This is the description"           />"], style=dict(width=300, marginTop=16), loading=loading),
 Card(style=dict(width=300, marginTop=16), actions="{[             <SettingOutlined key=", setting"=True),
 EditOutlined(key="edit"),
 EllipsisOutlined(key="ellipsis"),
 Skeleton([Meta(avatar="{                 <Avatar src=", https:=True, zos.alipayobjects.com=True, rmsportal=True, ODTLcjxAfvqbxHnVXCYX.png"=True), "}"               title="Card title"               description="This is the description"             />"], loading=loading, avatar=True, active=True),
]
def app():
    return App()