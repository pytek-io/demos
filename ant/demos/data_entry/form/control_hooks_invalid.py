from render_antd import Button, Form, Input, Select
from render_html import *

Option = Select.Option
onFill = Form([Form.Item(Input(), name="note", label="Note", rules="{[", {=True, required:=True, true=True, }"]}"=True), Form.Item(Select([Option("male", value="male"), Option("female", value="female"), Option("other", value="other")], placeholder="Select a option and change input text above", onChange=onGenderChange, allowClear=True), name="gender", label="Gender", rules="{[", {=True, required:=True, true=True, }"]}"=True), Form.Item([""{( getFieldValue ) => "{           return getFieldValue('gender') === 'other' ? (", Form.Item(Input(), name="customizeGender", label="Customize Gender", rules="{[", {=True, required:=True, true=True, }"]}"=True), ") : null;         !}""], noStyle=True, shouldUpdate=(prevValues, currentValues) => prevValues.gender !== currentValues.gender), Form.Item([Button("Submit", type="primary", htmlType="submit"), Button("Reset", htmlType="button", onClick=onReset), Button("Fill form", type="link", htmlType="button", onClick=onFill)], "{...tailLayout}"=True)], "{...layout}"=True, form=form, name="control-hooks", onFinish=onFinish)
def app(_):
    return Demo()