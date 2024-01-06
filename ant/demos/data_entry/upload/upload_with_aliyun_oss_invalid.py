from render_html import *
from render_antd import Form, Upload, message, Button
from render_ant_icons import UploadOutlined

onChange = this.onChange
value, onChange = this.value, this.onChange
OSSData = this.OSSData
OSSData = this.OSSData
value = this.value


def app():
    return Upload(Button("Click to Upload", icon=UploadOutlined([])), "{...props}"=True)


FormPage = Form(
    Form.Item(AliyunOSSUpload(), label="Photos", name="photos"), labelCol=dict(span=4)
)


def app():
    return FormPage()
