from reflect_html import *
from reflect_antd import Upload, Button
from reflect_ant_icons import UploadOutlined


def app():
    return Upload(Button("Upload", icon=UploadOutlined([])), "{...props}"=True)
