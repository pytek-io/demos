from render_antd import Col, InputNumber, Row, Slider
from render_html import *

inputValue = this.inputValue
inputValue = this.inputValue
def app():
    return Row([Col(Slider(min=1, max=20, onChange=this.onChange, value=typeof inputValue === 'number' ? inputValue : 0), span=12), Col(InputNumber(min=1, max=20, style=dict(margin='0 16px'), value=inputValue, onChange=this.onChange), span=4)])
def app():
    return Row([Col(Slider(min=0, max=1, onChange=this.onChange, value=typeof inputValue === 'number' ? inputValue : 0, step=0.01), span=12), Col(InputNumber(min=0, max=1, style=dict(margin='0 16px'), step=0.01, value=inputValue, onChange=this.onChange), span=4)])
def app():
    return div([IntegerStep(), DecimalStep()])