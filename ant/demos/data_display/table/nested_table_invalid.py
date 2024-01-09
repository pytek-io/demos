from render_ant_icons import DownOutlined
from render_antd import Badge, Dropdown, Menu, Space, Table
from render_html import *

menu = Menu([Menu.Item("Action 1"), Menu.Item("Action 2")])
expandedRowRender = Table(
    className="components-table-demo-nested",
    columns=columns,
    expandable=dict(),
    dataSource=data,
)


def app():
    return NestedTable()
