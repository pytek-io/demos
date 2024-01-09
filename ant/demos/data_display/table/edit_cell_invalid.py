from render_antd import Button, Form, Input, Popconfirm, Table
from render_antd.lib.form import FormInstance
from render_html import *

count, dataSource = this.count, this.dataSource
dataSource = this.dataSource
def app():
    return Form(EditableContext.Provider(tr("{...props}"=True), value=form), form=form, component=False)
toggleEdit = Form.Item(Input(ref=inputRef, onPressEnter=save, onBlur=save), style=dict(margin=0), name=dataIndex, rules="{[           ", {=True, required:=True, true,=True, message:=True, `$"{title}"=True, is=True, required.`,=True, }",=True, ]}"=True)
toggleEdit = div(""{children}"", className="editable-cell-value-wrap", style=dict(paddingRight=24), onClick=toggleEdit)
def app():
    return div([Button("Add a row", onClick=this.handleAdd, type="primary", style=dict(marginBottom=16)), Table(components=components, rowClassName=lambda :'editable-row', bordered=True, dataSource=dataSource, columns=columns as ColumnTypes)])
def app():
    return EditableTable()