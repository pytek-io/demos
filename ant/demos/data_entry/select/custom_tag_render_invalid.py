from render_html import *
from render_antd import Select, Tag
label, value, closable, onClose = props.label, props.value, props.closable, props.onClose
def app():
    return Tag(""{label}"", color=value, closable=closable, onClose=onClose, style=dict(marginRight=3))
def app():
    return Select(mode="multiple", showArrow=True, tagRender=tagRender, defaultValue=['gold', 'cyan'], style=dict(width='100%'), options=options)