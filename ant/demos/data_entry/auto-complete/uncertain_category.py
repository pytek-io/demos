from reflect_html import *
from reflect_antd import Input, AutoComplete


onSelect = AutoComplete(
    Input.Search(size="large", placeholder="input here", enterButton=True),
    dropdownMatchSelectWidth=252,
    style=dict(width=300),
    options=options,
    onSelect=onSelect,
    onSearch=handleSearch,
)


def app():
    return [
        Complete(),
    ]
