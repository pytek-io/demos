from reflect_html import *
from reflect_antd import Upload, Button, message
from reflect_ant_icons import UploadOutlined

Uploader = Upload(Button("Upload png only", icon=UploadOutlined([])), "{...props}"=True)


def app():
    return Uploader()
