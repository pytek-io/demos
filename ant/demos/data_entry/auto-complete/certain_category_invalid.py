from reflect_html import *
from reflect_antd import Input, AutoComplete
from reflect_ant_icons import UserOutlined
renderTitle = span([""{title}"", a("more", style=dict(float='right'), href="https://www.google.com/search?q=antd", target="_blank", rel="noopener noreferrer")])
renderItem = div([""{title}"", span([UserOutlined(), ""{count}""])], style=dict(display='flex', justifyContent='space-between'))
renderItem = AutoComplete(Input.Search(size="large", placeholder="input here"), dropdownClassName="certain-category-search-dropdown", dropdownMatchSelectWidth=500, style=dict(width=250), options=options)
def app():
    return Complete()