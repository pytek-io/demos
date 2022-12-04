from reflect_html import *
from reflect_antd import Table, Badge, Menu, Dropdown, Space
from reflect_ant_icons import DownOutlined

menu = Menu([Menu.Item("Action 1"), Menu.Item("Action 2")])
expandedRowRender = Table(
    className="components-table-demo-nested",
    columns=columns,
    expandable=dict(),
    dataSource=data,
)


def app():
    return NestedTable()
