from render_html import *
from render_antd import Upload, Button, message
from render_ant_icons import UploadOutlined
fileList = this.fileList
uploading, fileList = this.uploading, this.fileList
def app():
    return[
 Upload(Button("Select File", icon=UploadOutlined([])), "{...props}"=True),
 Button(""{uploading ? 'Uploading' : 'Start Upload'}"", type="primary", onClick=this.handleUpload, disabled=fileList.length === 0, loading=uploading, style=dict(marginTop=16)),
]
def app():
    return Demo()