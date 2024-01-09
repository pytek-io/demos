from render_antd import Avatar, List, Spin, message
from render_html import *

data = this.data
data = this.data
def app():
    return List.Item([List.Item.Meta(""{item.name.last}"", avatar="{Avatar(src=", https:=True, zos.alipayobjects.com=True, rmsportal=True, ODTLcjxAfvqbxHnVXCYX.png")}"=True, title="{a(href=", https:=True, ant.design"=True), "}"           description="{item.email}"         />", div("Content")], key=key, style=style)
vlist = VList(autoHeight=True, height=height, isScrolling=isScrolling, onScroll=onChildScroll, overscanRowCount=2, rowCount=data.length, rowHeight=73, rowRenderer=this.renderItem, onRowsRendered=onRowsRendered, scrollTop=scrollTop, width=width)
autoSize = AutoSizer(""{( width ) =>           vlist(             height,             isScrolling,             onChildScroll,             scrollTop,             onRowsRendered,             width,           )         }"", disableHeight=True)
infiniteLoader = InfiniteLoader(""{( onRowsRendered ) =>           autoSize(             height,             isScrolling,             onChildScroll,             scrollTop,             onRowsRendered,           )         }"", isRowLoaded=this.isRowLoaded, loadMoreRows=this.handleInfiniteOnLoad, rowCount=data.length)
def app():
    return List([""{data.length > 0 &&", WindowScroller(""{infiniteLoader}""), "}"         "{this.state.loading &&", Spin(className="demo-loading"), "}""])
def app():
    return VirtualizedExample()