from render_html import *
from render_antd import Tabs, Select
TabPane = Tabs.TabPane
Option = Select.Option
parentPos, childPos, parentType, childType = this.parentPos, this.childPos, this.parentType, this.childType
def app():
    return div([Select([""{positionList.map(pos => (", Option("Parent - "{pos}"", key=pos, value=pos), "))}""], style=dict(width=200), onChange="{val => ", {=True, this.setState(=True, parentPos:=True, val=True, );=True, !}"=True), Select([""{positionList.map(pos => (", Option("Child - "{pos}"", key=pos, value=pos), "))}""], style=dict(width=200), onChange="{val => ", {=True, this.setState(=True, childPos:=True, val=True, );=True, !}"=True), Select([Option("Parent - line", value="line"), Option("Parent - card", value="card"), Option("Parent - card edit", value="editable-card")], style=dict(width=200), onChange="{val => ", {=True, this.setState(=True, parentType:=True, val=True, );=True, !}"=True), Select([Option("Child - line", value="line"), Option("Child - card", value="card"), Option("Parent - card edit", value="editable-card")], style=dict(width=200), onChange="{val => ", {=True, this.setState(=True, childType:=True, val=True, );=True, !}"=True), Tabs([TabPane(Tabs([""{list.map(key => (", TabPane("TTTT "{key}"", tab="{`Tab $", {key}"`}"=True, key=key), "))}""], defaultActiveKey="1", tabPosition=childPos, type=childType, style=dict(height=300)), tab="Tab 1", key="1"), TabPane("Content of Tab Pane 2", tab="Tab 2", key="2")], defaultActiveKey="1", tabPosition=parentPos, type=parentType)])
def app():
    return Demo()