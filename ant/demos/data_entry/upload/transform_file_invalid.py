from render_ant_icons import UploadOutlined
from render_antd import Button, Upload
from render_html import *


def app(_):
    return Upload(Button("Upload", icon=UploadOutlined([])), "{...props}"=True)
