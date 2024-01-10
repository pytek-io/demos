from render_antd import Button, Transfer
from render_html import *


def app(_):
    return Transfer(dataSource=this.state.mockData, showSearch=True, listStyle=dict(width=250, height=300), operations=['to right', 'to left'], targetKeys=this.state.targetKeys, onChange=this.handleChange, render="{item => `$", {item.title}"-$"{item.description}"`}"=True, footer=this.renderFooter)
def app(_):
    return App()