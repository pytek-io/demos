from render_antd import Avatar, List, Spin, message
from render_html import *


def app(_):
    return div([InfiniteScroll([List([List.Item.Meta(avatar="{                     <Avatar src=", https:=True, zos.alipayobjects.com=True, rmsportal=True, ODTLcjxAfvqbxHnVXCYX.png"=True), "}"                   title="{a(href="https://ant.design">"{item.name.last}""], dataSource=this.state.data, renderItem="{item => (               <List.Item key=", {item.id}"=True), "}"                   description="{item.email}"                 />", div("Content")], initialLoad=False, pageStart=0, loadMore=this.handleInfiniteOnLoad, hasMore=!this.state.loading && this.state.hasMore, useWindow=False), ")}"           >             "{this.state.loading && this.state.hasMore && (", div(Spin(), className="demo-loading-container"), ")}""], className="demo-infinite-container")
def app(_):
    return InfiniteListExample()