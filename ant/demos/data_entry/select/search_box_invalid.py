from reflect_html import *
from reflect_antd import Select
Option = Select.Option
result = d.result
def app():
    return Select(""{options}"", showSearch=True, value=this.state.value, placeholder=this.props.placeholder, style=this.props.style, defaultActiveFirstOption=False, showArrow=False, filterOption=False, onSearch=this.handleSearch, onChange=this.handleChange, notFoundContent=null)
def app():
    return SearchInput(placeholder="input search text", style=dict(width=200))