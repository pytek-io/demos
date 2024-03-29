from render_antd import Select
from render_html import *

Option = Select.Option
def app(_):
    return Select([Option("Jack", value="jack"), Option("Lucy", value="lucy"), Option("Tom", value="tom")], showSearch=True, style=dict(width=200), placeholder="Select a person", optionFilterProp="children", onChange=onChange, onFocus=onFocus, onBlur=onBlur, onSearch=onSearch, filterOption=(input, option) =>       option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0)