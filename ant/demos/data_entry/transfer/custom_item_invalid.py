from render_antd import Transfer
from render_html import *

customLabel = span(""{item.title}" - "{item.description}"", className="custom-item")
def app(_):
    return Transfer(dataSource=this.state.mockData, listStyle=dict(width=300, height=300), targetKeys=this.state.targetKeys, onChange=this.handleChange, render=this.renderItem)
def app(_):
    return App()