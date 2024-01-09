from render_antd import Table
from render_html import *
from rendered.react.window import VariableSizeGrid as Grid

obj = dict()
columns, scroll = props.columns, props.scroll
width = mergedColumns.width
renderVirtualList = Grid(["scroll!.y! && index === mergedColumns.length - 1             ? (width as number) - scrollbarSize - 1             : (width as number);         !}"         height="{scroll!.y as number}"         rowCount="{rawData.length}"         rowHeight="{lambda :54}"         width="{tableWidth}"         onScroll="{( scrollLeft }": "{ scrollLeft: number ) => "{           onScroll( scrollLeft );         !}"       >         "{(           columnIndex,           rowIndex,           style,         }": "{           columnIndex: number;           rowIndex: number;           style: React.CSSProperties;         ) => (", div(""{(rawData[rowIndex] as any)[(mergedColumns as any)[columnIndex].dataIndex]}"", className="{classNames('virtual-table-cell', ", {=True, 'virtual-table-cell-last':=True, columnIndex="mergedColumns.length", -=True, 1,=True, )}"=True, style=style), ")}""], ref=gridRef, className="virtual-grid", columnCount=mergedColumns.length, columnWidth="{(index: number) => ", {=True, return=True, totalHeight=True)
def app():
    return ResizeObserver(Table("{...props}"=True, className="virtual-table", columns=mergedColumns, pagination=False, components=dict(body=renderVirtualList)), onResize="{( width ) => ", {=True, setTableWidth(width);=True, !}"=True)
def app():
    return VirtualTable(columns=columns, dataSource=data, scroll=dict(y=300, x='100vw'))