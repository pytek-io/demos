from render_ant_icons import LockOutlined, UserOutlined
from render_antd import Button, Form, Input
from render_html import *

onFinish = Form([Form.Item(Input(prefix="{UserOutlined(className=", site-form-item-icon")}"=True, placeholder="Username"), name="username", rules="{[", {=True, required:=True, true,=True, message:=True, 'Please=True, input=True, your=True, username!'=True, }"]}"=True), Form.Item(Input(prefix="{LockOutlined(className=", site-form-item-icon")}"=True, type="password", placeholder="Password"), name="password", rules="{[", {=True, required:=True, true,=True, message:=True, 'Please=True, input=True, your=True, password!'=True, }"]}"=True), Form.Item([""{lambda :(", Button("Log in", type="primary", htmlType="submit", disabled=!form.isFieldsTouched(true) ||               !!form.getFieldsError().filter(( errors ) => errors.length).length), ")}""], shouldUpdate=true)], form=form, name="horizontal_login", layout="inline", onFinish=onFinish)
def app(_):
    return HorizontalLoginForm()