from render_ant_icons import SmileOutlined
from render_html import *

style = dict(width=200)
customize = this.customize
customizeRenderEmpty = div([SmileOutlined(style=dict(fontSize=20)), p("Data Not Found")], style=dict(textAlign='center'))
def app(_):
    return div([Switch(unCheckedChildren="default", checkedChildren="customize", checked=customize, onChange="{val => ", {=True, this.setState(=True, customize:=True, val=True, );=True, !}"=True), Divider(), ConfigProvider(div([h4("Select"), Select(style=style), h4("TreeSelect"), TreeSelect(style=style, treeData=[]), h4("Cascader"), Cascader(style=style, options=[], showSearch=True), h4("Transfer"), Transfer(), h4("Table"), Table(style=dict(marginTop=8), columns="{[                 ", {=True, title:=True, 'Name',=True, dataIndex:=True, 'name',=True, key:=True, 'name',=True, }",=True, "{=True, title:=True, 'Age',=True, dataIndex:=True, 'age',=True, key:=True, 'age',=True, }",=True, ]}"=True), h4("List"), List()], className="config-provider"), renderEmpty=customize && customizeRenderEmpty)])
def app(_):
    return Demo()