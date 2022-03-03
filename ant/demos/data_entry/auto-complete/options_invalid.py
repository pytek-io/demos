from reflect_html import *
from reflect_antd import AutoComplete
Option = AutoComplete.Option
handleSearch = AutoComplete([""{result.map((email: string) => (", Option(""{email}"", key=email, value=email), "))}""], style=dict(width=200), onSearch=handleSearch, placeholder="input here")
def app():
    return Complete()