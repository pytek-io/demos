from render_ant_icons import SmileOutlined, UserOutlined
from render_antd import (Avatar, Button, Form, Input, InputNumber, Modal,
                         Typography)
from render_antd.lib.form import FormInstance
from render_html import *

basicForm = forms.basicForm
onOk = Modal(Form([Form.Item(Input(), name="name", label="User Name", rules="{[", {=True, required:=True, true=True, }"]}"=True), Form.Item(InputNumber(), name="age", label="User Age", rules="{[", {=True, required:=True, true=True, }"]}"=True)], form=form, layout="vertical", name="userForm"), title="Basic Drawer", visible=visible, onOk=onOk, onCancel=onCancel)
def app():
    return Demo()