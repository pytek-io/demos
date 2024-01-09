from render_antd import Form, Input, InputNumber, Popconfirm, Table, Typography
from render_html import *


def app():
    return td([""{editing ? (", Form.Item(""{inputNode}"", name=dataIndex, style=dict(margin=0), rules="{[             ", {=True, required:=True, true,=True, message:=True, `Please=True, Input=True, $"{title}"!`,=True, }",=True, ]}"=True), ") : (         children       )}""], "{...restProps}"=True)
row = span([a("Save", href="javascript:;", onClick=lambda :save(record.key), style=dict(marginRight=8)), Popconfirm(a("Cancel"), title="Sure to cancel?", onConfirm=cancel)])
row = Typography.Link("Edit", disabled=editingKey !== '', onClick=lambda :edit(record))
def app():
    return Form(Table(components="{!           body: ", {=True, cell:=True, EditableCell,=True, }",=True, !}"=True, bordered=True, dataSource=data, columns=mergedColumns, rowClassName="editable-row", pagination=dict(onChange=cancel)), form=form, component=False)
def app():
    return EditableTable()