from reflect_html import *
from reflect_antd import Transfer
customLabel = span(""{item.title}" - "{item.description}"", className="custom-item")
def app():
    return Transfer(dataSource=this.state.mockData, listStyle=dict(width=300, height=300), targetKeys=this.state.targetKeys, onChange=this.handleChange, render=this.renderItem)
def app():
    return App()