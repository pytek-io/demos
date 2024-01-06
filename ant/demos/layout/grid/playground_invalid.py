from render_html import *
from render_antd import Row, Col, Slider
gutters = dict()
vgutters = dict()
colCounts = dict()
gutterKey, vgutterKey, colCountKey = this.gutterKey, this.vgutterKey, this.colCountKey
def app():
    return[
 span("Horizontal Gutter (px):"),
 div(Slider(min=0, max=Object.keys(gutters).length - 1, value=gutterKey, onChange=this.onGutterChange, marks=gutters, step=null, tipFormatter=valulambda e:gutters[value]), style=dict(width='50%')),
 span("Vertical Gutter (px):"),
 div(Slider(min=0, max=Object.keys(vgutters).length - 1, value=vgutterKey, onChange=this.onVGutterChange, marks=vgutters, step=null, tipFormatter=valulambda e:vgutters[value]), style=dict(width='50%')),
 span("Column Count:"),
 div(Slider(min=0, max=Object.keys(colCounts).length - 1, value=colCountKey, onChange=this.onColCountChange, marks=colCounts, step=null, tipFormatter=valulambda e:colCounts[value]), style=dict(width='50%', marginBottom=48)),
 Row(""{cols}"           "{cols}"", gutter=[gutters[gutterKey], vgutters[vgutterKey]]),
 Row(""{cols}"", gutter=[gutters[gutterKey], vgutters[vgutterKey]]),
 pre([""{`", Row("\n$"{colCode}"\n$"{colCode}"", gutter="{[$", {gutters[gutterKey]}",=True, $"{vgutters[vgutterKey]}"]}"=True), "`}""], className="demo-code"),
 pre([""{`", Row("\n$"{colCode}"", gutter="{[$", {gutters[gutterKey]}",=True, $"{vgutters[vgutterKey]}"]}"=True), "`}""], className="demo-code"),
]
def app():
    return App()