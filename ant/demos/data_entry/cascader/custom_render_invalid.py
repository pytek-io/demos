from reflect_html import *
from reflect_antd import Cascader
displayRender = span([""{label}" (", a(""{option.code}"", onClick=lambda e:handleAreaClick(e, label, option)), ")"], key=option.value)
def app():
    return Cascader(options=options, defaultValue=['zhejiang', 'hangzhou', 'xihu'], displayRender=displayRender, style=dict(width='100%'))