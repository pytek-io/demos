from render_html import *
from render_ant_icons import DownOutlined, ClockCircleOutlined
Panel = Collapse.Panel
TreeNode = Tree.TreeNode
TabPane = Tabs.TabPane
Meta = Card.Meta
Link = Anchor.Link
Text = Typography.Text
disabled, selectedKeys, targetKeys, showSearch = this.disabled, this.selectedKeys, this.targetKeys, this.showSearch
TableTransfer = Table(id="components-transfer-table", rowSelection=rowSelection, columns=columns, dataSource=filteredItems, size="small", style=dict(pointerEvents=listDisabled ? 'none' : null), onRow="{( key, disabled: itemDisabled ) => (             onClick: lambda :", {=True, if=True, (itemDisabled=True, ||=True, listDisabled)=True, return;=True, onItemSelect(key,=True, !listSelectedKeys.includes(key));=True, }",=True, )}"=True)
def app():
    return[
 tr([th("Total"), td(Text(""{totalBorrow}"", type="danger")), td(Text(""{totalRepayment}""))]),
 tr([th("Balance"), td(Text(""{totalBorrow - totalRepayment}"", type="danger"), colSpan=2)]),
]
def app():
    return App()