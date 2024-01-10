from render_antd import Switch, Table, Tag, Transfer
from render_html import *

targetKeys, disabled, showSearch = this.targetKeys, this.disabled, this.showSearch
TableTransfer = Table(rowSelection=rowSelection, columns=columns, dataSource=filteredItems, size="small", style=dict(pointerEvents=listDisabled ? 'none' : null), onRow="{( key, disabled: itemDisabled ) => (             onClick: lambda :", {=True, if=True, (itemDisabled=True, ||=True, listDisabled)=True, return;=True, onItemSelect(key,=True, !listSelectedKeys.includes(key));=True, }",=True, )}"=True)
def app(_):
    return[
 TableTransfer(dataSource=mockData, targetKeys=targetKeys, disabled=disabled, showSearch=showSearch, onChange=this.onChange, filterOption=(inputValue, item) =>             item.title.indexOf(inputValue) !== -1 || item.tag.indexOf(inputValue) !== -1, leftColumns=leftTableColumns, rightColumns=rightTableColumns),
 Switch(unCheckedChildren="disabled", checkedChildren="disabled", checked=disabled, onChange=this.triggerDisable, style=dict(marginTop=16)),
 Switch(unCheckedChildren="showSearch", checkedChildren="showSearch", checked=showSearch, onChange=this.triggerShowSearch, style=dict(marginTop=16)),
]
def app(_):
    return App()