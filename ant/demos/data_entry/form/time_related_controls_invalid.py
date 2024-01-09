from render_antd import Button, DatePicker, Form, TimePicker
from render_html import *

RangePicker = DatePicker.RangePicker
onFinish = Form([Form.Item(DatePicker(), name="date-picker", label="DatePicker", "{...config}"=True), Form.Item(DatePicker(showTime=True, format="YYYY-MM-DD HH:mm:ss"), name="date-time-picker", label="DatePicker[showTime]", "{...config}"=True), Form.Item(DatePicker(picker="month"), name="month-picker", label="MonthPicker", "{...config}"=True), Form.Item(RangePicker(), name="range-picker", label="RangePicker", "{...rangeConfig}"=True), Form.Item(RangePicker(showTime=True, format="YYYY-MM-DD HH:mm:ss"), name="range-time-picker", label="RangePicker[showTime]", "{...rangeConfig}"=True), Form.Item(TimePicker(), name="time-picker", label="TimePicker", "{...config}"=True), Form.Item(Button("Submit", type="primary", htmlType="submit"), wrapperCol="{!           xs: ", {=True, span:=True, 24,=True, offset:=True, 0=True, }",=True, sm:=True, "{=True, span:=True, 16,=True, offset:=True, 8=True, }",=True, !}"=True)], name="time_related_controls", "{...formItemLayout}"=True, onFinish=onFinish)
def app():
    return TimeRelatedForm()