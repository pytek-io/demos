from reflect_html import *
from reflect_antd import Form, InputNumber
onNumberChange = Form(Form.Item(InputNumber(min=8, max=12, value=number.value, onChange=onNumberChange), "{...formItemLayout}"=True, label="Prime between 8 & 12", validateStatus=number.validateStatus, help=number.errorMsg || tips))
def app():
    return RawForm()