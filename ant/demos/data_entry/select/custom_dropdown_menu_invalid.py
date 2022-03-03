from reflect_html import *
from reflect_antd import Select, Divider, Input
from reflect_ant_icons import PlusOutlined
Option = Select.Option
items, name = this.items, this.name
items, name = this.items, this.name
def app():
    return[
 Select(style=dict(width=240), placeholder="custom dropdown render", dropdownRender="{menu => (           <div>             ", {menu}"=True, <Divider=True, style=dict(margin='4px 0')),
 div([Input(style=dict(flex='auto'), value=name, onChange=this.onNameChange), a([PlusOutlined(), "Add item"], style=dict(flex='none', padding='8px', display='block', cursor='pointer'), onClick=this.addItem)], style=dict(display='flex', flexWrap='nowrap', padding=8)),
 Option(""{item}"", key=item),
]
def app():
    return App()