from reflect_html import *
from reflect_antd import Select
Option = Select.Option
def app():
    return Select([Option("Not Identified", value="1"), Option("Closed", value="2"), Option("Communicated", value="3"), Option("Identified", value="4"), Option("Resolved", value="5"), Option("Cancelled", value="6")], showSearch=True, style=dict(width=200), placeholder="Search to Select", optionFilterProp="children", filterOption=(input, option) =>       option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0, filterSort=(optionA, optionB) =>       optionA.children.toLowerCase().localeCompare(optionB.children.toLowerCase()))