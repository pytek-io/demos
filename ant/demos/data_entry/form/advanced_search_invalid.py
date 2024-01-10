from render_ant_icons import DownOutlined, UpOutlined
from render_antd import Button, Col, Form, Input, Row
from render_html import *

getFields = Col(Form.Item(Input(placeholder="placeholder"), name="{`field-$", {i}"`}"=True, label="{`Field $", {i}"`}"=True, rules="{[               ", {=True, required:=True, true,=True, message:=True, 'Input=True, something!',=True, }",=True, ]}"=True), span=8, key=i)
onFinish = Form([Row(""{getFields()}"", gutter=24), Row(Col([Button("Search", type="primary", htmlType="submit"), Button("Clear", style=dict(margin='0 8px'), onClick="{lambda :", {=True, form.resetFields();=True, !}"=True), a([""{expand ?", UpOutlined(), ":", DownOutlined(), "}" Collapse"], style=dict(fontSize=12), onClick="{lambda :", {=True, setExpand(!expand);=True, !}"=True)], span=24, style=dict(textAlign='right')))], form=form, name="advanced_search", className="ant-advanced-search-form", onFinish=onFinish)
def app(_):
    return div([AdvancedSearchForm(), div("Search Result List", className="search-result-list")])