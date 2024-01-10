from render_antd import Cascader
from render_html import *

displayRender = span([""{label}" (", a(""{option.code}"", onClick=lambda e:handleAreaClick(e, label, option)), ")"], key=option.value)
def app(_):
    return Cascader(options=options, defaultValue=['zhejiang', 'hangzhou', 'xihu'], displayRender=displayRender, style=dict(width='100%'))