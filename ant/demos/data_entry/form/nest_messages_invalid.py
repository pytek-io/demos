from render_antd import Button, Form, Input, InputNumber
from render_html import *

onFinish = Form([Form.Item(Input(), name=['user', 'name'], label="Name", rules="{[", {=True, required:=True, true=True, }"]}"=True), Form.Item(Input(), name=['user', 'email'], label="Email", rules="{[", {=True, type:=True, 'email'=True, }"]}"=True), Form.Item(InputNumber(), name=['user', 'age'], label="Age", rules="{[", {=True, type:=True, 'number',=True, min:=True, 0,=True, max:=True, 99=True, }"]}"=True), Form.Item(Input(), name=['user', 'website'], label="Website"), Form.Item(Input.TextArea(), name=['user', 'introduction'], label="Introduction"), Form.Item(Button("Submit", type="primary", htmlType="submit"), wrapperCol=dict(offset=8))], "{...layout}"=True, name="nest-messages", onFinish=onFinish, validateMessages=validateMessages)
def app(_):
    return Demo()