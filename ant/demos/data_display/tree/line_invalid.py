from reflect_html import *
from reflect_antd import Tree, Switch
from reflect_ant_icons import CarryOutOutlined, FormOutlined
def app():
    return[
 div("multiple line title"),
 div("multiple line title"),
]
onSetShowLine = div([div(["showLine:", Switch(checked=!!showLine, onChange=onSetShowLine), br(), br(), "showIcon:", Switch(checked=showIcon, onChange=setShowIcon), br(), br(), "showLeafIcon:", Switch(checked=showLeafIcon, onChange=onSetLeafIcon)], style=dict(marginBottom=16)), Tree(showLine=showLine, showIcon=showIcon, defaultExpandedKeys=['0-0-0'], onSelect=onSelect, treeData=treeData)])
def app():
    return Demo()