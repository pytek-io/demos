from render_antd import Button, Checkbox, Form, Input
from render_html import *

onCheckboxChange = Form([Form.Item(Input(placeholder="Please input your name"), "{...formItemLayout}"=True, name="username", label="Name", rules="{[           ", {=True, required:=True, true,=True, message:=True, 'Please=True, input=True, your=True, name',=True, }",=True, ]}"=True), Form.Item(Input(placeholder="Please input your nickname"), "{...formItemLayout}"=True, name="nickname", label="Nickname", rules="{[           ", {=True, required:=True, checkNick,=True, message:=True, 'Please=True, input=True, your=True, nickname',=True, }",=True, ]}"=True), Form.Item(Checkbox("Nickname is required", checked=checkNick, onChange=onCheckboxChange), "{...formTailLayout}"=True), Form.Item(Button("Check", type="primary", onClick=onCheck), "{...formTailLayout}"=True)], form=form, name="dynamic_rule")
def app(_):
    return DynamicRule()