from render_html import *
from render_antd import Table
from rendered.react.dnd import DndProvider, useDrag, useDrop, createDndContext
from rendered.react.dnd.html5.backend import HTML5Backend
index: dragIndex = monitor.index: dragIndex
DragableBodyRow = tr(ref=ref, className="{`$", {className}"$"{isOver=True, ?=True, dropClassName=True, :=True, ''}"`}"=True, style=dict(cursor='move'), "{...restProps}"=True)
def app():
    return DndProvider(Table(columns=columns, dataSource=data, components=components, onRow=(record, index) => (           index,           moveRow,         )), manager=manager.current.dragDropManager)
def app():
    return DragSortingTable()