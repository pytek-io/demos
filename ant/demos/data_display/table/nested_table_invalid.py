from render_html import *
from render_antd import Table, Badge, Menu, Dropdown, Space
from render_ant_icons import DownOutlined

menu = Menu([Menu.Item("Action 1"), Menu.Item("Action 2")])
expandedRowRender = Table(
    className="components-table-demo-nested",
    columns=columns,
    expandable=dict(),
    dataSource=data,
)


def app():
    return NestedTable()
