from render_html import *
from render_antd import Upload, Button
from render_ant_icons import UploadOutlined


def app():
    return Upload(Button("Upload", icon=UploadOutlined([])), "{...props}"=True)
