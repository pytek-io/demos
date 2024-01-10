from render_ant_icons import UploadOutlined
from render_antd import Button, Form, Upload, message
from render_html import *

onChange = this.onChange
value, onChange = this.value, this.onChange
OSSData = this.OSSData
OSSData = this.OSSData
value = this.value


def app(_):
    return Upload(Button("Click to Upload", icon=UploadOutlined([])), "{...props}"=True)


FormPage = Form(
    Form.Item(AliyunOSSUpload(), label="Photos", name="photos"), labelCol=dict(span=4)
)


def app(_):
    return FormPage()
