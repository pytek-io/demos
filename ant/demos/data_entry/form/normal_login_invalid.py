from render_ant_icons import LockOutlined, UserOutlined
from render_antd import Button, Checkbox, Form, Input
from render_html import *

onFinish = Form([Form.Item(Input(prefix="{UserOutlined(className=", site-form-item-icon")}"=True, placeholder="Username"), name="username", rules="{[", {=True, required:=True, true,=True, message:=True, 'Please=True, input=True, your=True, Username!'=True, }"]}"=True), Form.Item(Input(prefix="{LockOutlined(className=", site-form-item-icon")}"=True, type="password", placeholder="Password"), name="password", rules="{[", {=True, required:=True, true,=True, message:=True, 'Please=True, input=True, your=True, Password!'=True, }"]}"=True), Form.Item([Form.Item(Checkbox("Remember me"), name="remember", valuePropName="checked", noStyle=True), a("Forgot password", className="login-form-forgot", href="")]), Form.Item([Button("Log in", type="primary", htmlType="submit", className="login-form-button"), "Or", a("register now!", href="")])], name="normal_login", className="login-form", initialValues=dict(remember=true), onFinish=onFinish)
def app():
    return NormalLoginForm()