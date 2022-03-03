from reflect_html import *
from reflect_antd import Upload, Button
from reflect_ant_icons import UploadOutlined


def app():
    return Upload(
        Button("Upload Directory", icon=UploadOutlined([])),
        action="https://www.mocky.io/v2/5cc8019d300000980a055e76",
        directory=True,
    )
