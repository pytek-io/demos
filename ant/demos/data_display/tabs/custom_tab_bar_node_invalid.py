from reflect_html import *
from reflect_antd import Tabs
from reflected.react.dnd import DndProvider, DragSource, DropTarget
from reflected.react.dnd.html5.backend import HTML5Backend
TabPane = Tabs.TabPane
connectDragSource, connectDropTarget, children = this.connectDragSource, this.connectDropTarget, this.children
children = this.children
order = this.order
children = this.children
def app():
    return DndProvider(Tabs(""{orderTabs}"", renderTabBar=this.renderTabBar, "{...this.props}"=True), backend=HTML5Backend)
def app():
    return DraggableTabs([TabPane("Content of Tab Pane 1", tab="tab 1", key="1"), TabPane("Content of Tab Pane 2", tab="tab 2", key="2"), TabPane("Content of Tab Pane 3", tab="tab 3", key="3")])