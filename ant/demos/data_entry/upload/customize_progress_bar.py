from reflect_html import *
from reflect_antd import Upload, message, Button
from reflect_ant_icons import UploadOutlined


def app():
    return Upload(Button("Click to Upload", icon=UploadOutlined([])))
