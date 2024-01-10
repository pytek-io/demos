from render_antd import Cascader
from render_html import *


def app(_):
    return span([""{this.state.text}"", Cascader(a("Change city", href="#"), options=options, onChange=this.onChange)])
def app(_):
    return CitySwitcher()