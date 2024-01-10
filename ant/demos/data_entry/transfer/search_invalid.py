from render_antd import Transfer
from render_html import *


def app(_):
    return Transfer(dataSource=this.state.mockData, showSearch=True, filterOption=this.filterOption, targetKeys=this.state.targetKeys, onChange=this.handleChange, onSearch=this.handleSearch, render=item => item.title)
def app(_):
    return App()