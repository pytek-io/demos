from render_html import *
from render_antd import Form, Input, Select, Button
Option = Select.Option
onCurrencyChange = span([Input(type="text", value=value.number || number, onChange=onNumberChange, style=dict(width=100)), Select([Option("RMB", value="rmb"), Option("Dollar", value="dollar")], value=value.currency || currency, style=dict(width=80, margin='0 8px'), onChange=onCurrencyChange)])
checkPrice = Form([Form.Item(PriceInput(), name="price", label="Price", rules="{[", {=True, validator:=True, checkPrice=True, }"]}"=True), Form.Item(Button("Submit", type="primary", htmlType="submit"))], name="customized_form_controls", layout="inline", onFinish=onFinish, initialValues="{!         price: ", {=True, number:=True, 0,=True, currency:=True, 'rmb',=True, }",=True, !}"=True)
def app():
    return Demo()