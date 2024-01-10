from render_ant_icons import MinusCircleOutlined, PlusOutlined
from render_antd import Button, Form, Input, Select, Space
from render_html import *

Option = Select.Option
handleChange = Space([Form.Item([""{lambda :(", Form.Item(Select([""{(sights[form.getFieldValue('area')] || []).map(item => (", Option(""{item}"", key=item, value=item), "))}""], disabled=!form.getFieldValue('area'), style=dict(width=130)), "{...field}"=True, label="Sight", name=[field.name, 'sight'], fieldKey=[field.fieldKey, 'sight'], rules="{[", {=True, required:=True, true,=True, message:=True, 'Missing=True, sight'=True, }"]}"=True), ")}""], noStyle=True, shouldUpdate=(prevValues, curValues) =>                     prevValues.area !== curValues.area || prevValues.sights !== curValues.sights), Form.Item(Input(), "{...field}"=True, label="Price", name=[field.name, 'price'], fieldKey=[field.fieldKey, 'price'], rules="{[", {=True, required:=True, true,=True, message:=True, 'Missing=True, price'=True, }"]}"=True), MinusCircleOutlined(onClick=lambda :remove(field.name))], key=field.key, align="baseline")
handleChange = Form.Item(Button("Add sights", type="dashed", onClick=lambda :add(), block=True, icon=<PlusOutlined />))
def app(_):
    return Demo()