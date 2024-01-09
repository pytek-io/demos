from render_ant_icons import UploadOutlined
from render_antd import Button, Upload
from render_html import *


def app():
    return[
 Upload(Button("Upload", icon=UploadOutlined([])), action="https://www.mocky.io/v2/5cc8019d300000980a055e76", listType="picture", defaultFileList=[...fileList]),
 br(),
 br(),
 Upload(Button("Upload", icon=UploadOutlined([])), action="https://www.mocky.io/v2/5cc8019d300000980a055e76", listType="picture", defaultFileList=[...fileList], className="upload-list-inline"),
]