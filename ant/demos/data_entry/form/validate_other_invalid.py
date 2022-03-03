from reflect_html import *
from reflect_ant_icons import UploadOutlined, InboxOutlined
Option = Select.Option
onFinish = Form([Form.Item(span("China", className="ant-form-text"), label="Plain Text"), Form.Item(Select([Option("China", value="china"), Option("U.S.A", value="usa")], placeholder="Please select a country"), name="select", label="Select", hasFeedback=True, rules="{[", {=True, required:=True, true,=True, message:=True, 'Please=True, select=True, your=True, country!'=True, }"]}"=True), Form.Item(Select([Option("Red", value="red"), Option("Green", value="green"), Option("Blue", value="blue")], mode="multiple", placeholder="Please select favourite colors"), name="select-multiple", label="Select[multiple]", rules="{[", {=True, required:=True, true,=True, message:=True, 'Please=True, select=True, your=True, favourite=True, colors!',=True, type:=True, 'array'=True, }"]}"=True), Form.Item([Form.Item(InputNumber(min=1, max=10), name="input-number", noStyle=True), span("machines", className="ant-form-text")], label="InputNumber"), Form.Item(Switch(), name="switch", label="Switch", valuePropName="checked"), Form.Item(Slider(marks=dict(0='A', 20='B', 40='C', 60='D', 80='E', 100='F')), name="slider", label="Slider"), Form.Item(Radio.Group([Radio("item 1", value="a"), Radio("item 2", value="b"), Radio("item 3", value="c")]), name="radio-group", label="Radio.Group"), Form.Item(Radio.Group([Radio.Button("item 1", value="a"), Radio.Button("item 2", value="b"), Radio.Button("item 3", value="c")]), name="radio-button", label="Radio.Button", rules="{[", {=True, required:=True, true,=True, message:=True, 'Please=True, pick=True, an=True, item!'=True, }"]}"=True), Form.Item(Checkbox.Group(Row([Col(Checkbox("A", value="A", style=dict(lineHeight='32px')), span=8), Col(Checkbox("B", value="B", style=dict(lineHeight='32px'), disabled=True), span=8), Col(Checkbox("C", value="C", style=dict(lineHeight='32px')), span=8), Col(Checkbox("D", value="D", style=dict(lineHeight='32px')), span=8), Col(Checkbox("E", value="E", style=dict(lineHeight='32px')), span=8), Col(Checkbox("F", value="F", style=dict(lineHeight='32px')), span=8)])), name="checkbox-group", label="Checkbox.Group"), Form.Item(Rate(), name="rate", label="Rate"), Form.Item(Upload(Button("Click to upload", icon=UploadOutlined([])), name="logo", action="/upload.do", listType="picture"), name="upload", label="Upload", valuePropName="fileList", getValueFromEvent=normFile, extra="longgggggggggggggggggggggggggggggggggg"), Form.Item(Form.Item(Upload.Dragger([p(InboxOutlined(), className="ant-upload-drag-icon"), p("Click or drag file to this area to upload", className="ant-upload-text"), p("Support for a single or bulk upload.", className="ant-upload-hint")], name="files", action="/upload.do"), name="dragger", valuePropName="fileList", getValueFromEvent=normFile, noStyle=True), label="Dragger"), Form.Item(Button("Submit", type="primary", htmlType="submit"), wrapperCol=dict(span=12, offset=6))], name="validate_other", "{...formItemLayout}"=True, onFinish=onFinish, initialValues=dict(['input-number']=3, ['checkbox-group']=['A', rate=3.5))
def app():
    return Demo()