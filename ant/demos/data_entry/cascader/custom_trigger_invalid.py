from reflect_html import *
from reflect_antd import Cascader
def app():
    return span([""{this.state.text}"", Cascader(a("Change city", href="#"), options=options, onChange=this.onChange)])
def app():
    return CitySwitcher()