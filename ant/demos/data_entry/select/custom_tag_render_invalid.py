from render_antd import Select, Tag
from render_html import *

label, value, closable, onClose = props.label, props.value, props.closable, props.onClose
def app(_):
    return Tag(""{label}"", color=value, closable=closable, onClose=onClose, style=dict(marginRight=3))
def app(_):
    return Select(mode="multiple", showArrow=True, tagRender=tagRender, defaultValue=['gold', 'cyan'], style=dict(width='100%'), options=options)