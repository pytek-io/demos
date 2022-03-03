from reflect_html import *
from reflect_antd import Skeleton, Switch, List, Avatar
from reflect_ant_icons import StarOutlined, LikeOutlined, MessageOutlined
loading = this.loading
IconText = span(""{React.createElement(icon, "{ style: "{ marginRight: 8 }" )}"     "{text}"")
def app():
    return[
 Switch(checked=!loading, onChange=this.onChange),
 List(itemLayout="vertical", size="large", dataSource=listData, renderItem="{item => (             <List.Item               key=", {item.title}"=True, actions="{                 !loading && [                   <IconText icon=", {StarOutlined}"=True, text="156", key="list-vertical-star-o"),
 IconText(icon=LikeOutlined, text="156", key="list-vertical-like-o"),
 IconText(icon=MessageOutlined, text="2", key="list-vertical-message"),
 img(width=272, alt="logo", src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png"),
 Skeleton([List.Item.Meta(""{item.title}"", avatar="{Avatar(src=", {item.avatar)}"=True, title="{a(href=", {item.href}"=True), "}"                   description="{item.description}"                 />                 "{item.content}""], loading=loading, active=True, avatar=True),
]
def app():
    return App()