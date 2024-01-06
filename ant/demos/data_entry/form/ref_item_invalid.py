from render_html import *
from render_antd import Button, Form, Input
def app():
    return Form([Form.Item(Input(ref=ref), name="test", label="test"), Form.List([""{fields =>           fields.map(field => (", Form.Item(Input(ref=ref), key=field.key, "{...field}"=True), "))         }""], name="list"), Button("Focus Form.Item", type="button", onClick="{lambda :", {=True, form.getFieldInstance('test').focus();=True, !}"=True), Button("Focus Form.List", onClick="{lambda :", {=True, form.getFieldInstance(['list',=True, 0]).focus();=True, !}"=True)], form=form, initialValues=dict(list=['light']))
def app():
    return Demo()