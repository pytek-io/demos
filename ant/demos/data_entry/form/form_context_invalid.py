from reflect_html import *
from reflect_antd import Form, Input, InputNumber, Modal, Button, Avatar, Typography
from reflect_ant_icons import SmileOutlined, UserOutlined
from reflect_antd.lib.form import FormInstance
basicForm = forms.basicForm
onOk = Modal(Form([Form.Item(Input(), name="name", label="User Name", rules="{[", {=True, required:=True, true=True, }"]}"=True), Form.Item(InputNumber(), name="age", label="User Age", rules="{[", {=True, required:=True, true=True, }"]}"=True)], form=form, layout="vertical", name="userForm"), title="Basic Drawer", visible=visible, onOk=onOk, onCancel=onCancel)
def app():
    return Demo()