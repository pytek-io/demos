from render import Callback
from render_ant_icons import MinusCircleOutlined, PlusOutlined
from render_antd import Button, Form, Input
from render_html import *


# DynamicFieldSet = Form.Item(
#     [Form.Item(Input(placeholder="passenger name",
#     style=dict(width='60%')), "{...field}"=True,
#     validateTrigger=['onChange', 'onBlur'], rules="{[                     ", {=True, required:=True, true,=True, whitespace:=True, true,=True, message:=True, "Please=True, input=True, passenger's=True, name=True, or=True, delete=True, this=True, field.",=True, }",=True, ]}"=True, noStyle=True), ""{fields.length > 1 ? (", MinusCircleOutlined(className="dynamic-delete-button", onClick=lambda :remove(field.name)), ") : null}""], "{...(index="0", ?=True, formItemLayout=True, :=True, formItemLayoutWithOutLabel)}"=True, label=index === 0 ? 'Passengers' : '', required=False, key=field.key)
# DynamicFieldSet = Form.Item([Button("Add field", type="dashed", onClick=lambda :add(), style=dict(width='60%'), icon=<PlusOutlined />), Button("Add field at head", type="dashed", onClick="{lambda :", {=True, add('The=True, head=True, item',=True, 0);=True, !}"=True, style=dict(width='60%', marginTop='20px'), icon=<PlusOutlined />), Form.ErrorList(errors=errors)])
def app(_):
    return Form(
        Form.List(
            [Form.Item() for ]
        )
        onFinish=Callback(
            lambda values: print("Success", values)
        ),
        name="dynamic_form_item",
    )