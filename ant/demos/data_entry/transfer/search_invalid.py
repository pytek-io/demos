from reflect_html import *
from reflect_antd import Transfer
def app():
    return Transfer(dataSource=this.state.mockData, showSearch=True, filterOption=this.filterOption, targetKeys=this.state.targetKeys, onChange=this.handleChange, onSearch=this.handleSearch, render=item => item.title)
def app():
    return App()