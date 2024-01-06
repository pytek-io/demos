from render_html import *
from render_antd import Input, Button
TextArea = Input.TextArea
autoResize = this.autoResize
def app():
    return[
 Button("Auto Resize: "{String(autoResize)}"", onClick=lambda :this.setState( autoResize: !autoResize ), style=dict(marginBottom=16)),
 TextArea(rows=4, autoSize=autoResize, defaultValue=defaultValue),
]
def app():
    return Demo()