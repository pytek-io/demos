from render_antd import Switch, Transfer
from render_html import *

targetKeys, selectedKeys, disabled = this.targetKeys, this.selectedKeys, this.disabled
def app(_):
    return[
 Transfer(dataSource=mockData, titles=['Source', 'Target'], targetKeys=targetKeys, selectedKeys=selectedKeys, onChange=this.handleChange, onSelectChange=this.handleSelectChange, onScroll=this.handleScroll, render=item => item.title, disabled=disabled, oneWay=True, style=dict(marginBottom=16)),
 Switch(unCheckedChildren="disabled", checkedChildren="disabled", checked=disabled, onChange=this.handleDisable),
]
def app(_):
    return App()