from reflect_html import *
from reflect_antd import Upload, Button
from reflect_ant_icons import UploadOutlined

Uploader = Upload(Button("Upload png only", icon=UploadOutlined([])))


def app():
    return Uploader()
