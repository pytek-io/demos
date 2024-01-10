from render_ant_icons import LikeOutlined, MessageOutlined, StarOutlined
from render_antd import Avatar, List, Skeleton, Switch
from render_html import *

loading = this.loading
IconText = span(""{React.createElement(icon, "{ style: "{ marginRight: 8 }" )}"     "{text}"")
def app(_):
    return[
 Switch(checked=!loading, onChange=this.onChange),
 List(itemLayout="vertical", size="large", dataSource=listData, renderItem="{item => (             <List.Item               key=", {item.title}"=True, actions="{                 !loading && [                   <IconText icon=", {StarOutlined}"=True, text="156", key="list-vertical-star-o"),
 IconText(icon=LikeOutlined, text="156", key="list-vertical-like-o"),
 IconText(icon=MessageOutlined, text="2", key="list-vertical-message"),
 img(width=272, alt="logo", src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png"),
 Skeleton([List.Item.Meta(""{item.title}"", avatar="{Avatar(src=", {item.avatar)}"=True, title="{a(href=", {item.href}"=True), "}"                   description="{item.description}"                 />                 "{item.content}""], loading=loading, active=True, avatar=True),
]
def app(_):
    return App()