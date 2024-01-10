from render_ant_icons import UploadOutlined
from render_antd import Button, Upload, message
from render_html import *

fileList = this.fileList
uploading, fileList = this.uploading, this.fileList
def app(_):
    return[
 Upload(Button("Select File", icon=UploadOutlined([])), "{...props}"=True),
 Button(""{uploading ? 'Uploading' : 'Start Upload'}"", type="primary", onClick=this.handleUpload, disabled=fileList.length === 0, loading=uploading, style=dict(marginTop=16)),
]
def app(_):
    return Demo()