from render_antd import DatePicker, Space
from render_html import *

style = dict()
RangePicker = DatePicker.RangePicker
def app():
    return div(""{current.date()}"", className="ant-picker-cell-inner", style=style)
def app():
    return div(""{current.date()}"", className="ant-picker-cell-inner", style=style)