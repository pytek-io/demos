from render_html import *
from render_antd import Upload, Button
from render_ant_icons import UploadOutlined

Uploader = Upload(Button("Upload png only", icon=UploadOutlined([])))


def app():
    return Uploader()
