from reflect_html import *
from reflect_antd import DatePicker, Space
RangePicker = DatePicker.RangePicker
def app():
    return Space([RangePicker(ranges=dict(Today=[moment(), 'This Month'=[moment().startOf('month')), onChange=onChange), RangePicker(ranges=dict(Today=[moment(), 'This Month'=[moment().startOf('month')), showTime=True, format="YYYY/MM/DD HH:mm:ss", onChange=onChange)], direction="vertical", size=12)