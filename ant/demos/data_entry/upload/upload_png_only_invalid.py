from render_ant_icons import UploadOutlined
from render_antd import Button, Upload
from render_html import *

Uploader = Upload(Button("Upload png only", icon=UploadOutlined([])))


def app():
    return Uploader()
