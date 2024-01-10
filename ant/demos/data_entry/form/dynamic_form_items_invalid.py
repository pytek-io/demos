from render_ant_icons import MinusCircleOutlined, PlusOutlined
from render_antd import Button, Form, Input, Space
from render_html import *


def app(_):
    return[
 Space([Form.Item(Input(placeholder="First Name"), "{...field}"=True, name=[field.name, 'first'], fieldKey=[field.fieldKey, 'first'], rules="{[", {=True, required:=True, true,=True, message:=True, 'Missing=True, first=True, name'=True, }"]}"=True), Form.Item(Input(placeholder="Last Name"), "{...field}"=True, name=[field.name, 'last'], fieldKey=[field.fieldKey, 'last'], rules="{[", {=True, required:=True, true,=True, message:=True, 'Missing=True, last=True, name'=True, }"]}"=True), MinusCircleOutlined(onClick=lambda :remove(field.name))], key=field.key, style=dict(display='flex', marginBottom=8), align="baseline"),
 Form.Item(Button("Add field", type="dashed", onClick=lambda :add(), block=True, icon=<PlusOutlined />)),
]
def app(_):
    return Demo()