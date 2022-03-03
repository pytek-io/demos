from reflect_html import *
from reflect_antd import Button, Radio
from reflect_ant_icons import DownloadOutlined
from reflect import autorun

def app():

    size = Radio.Group(
        [
            Radio.Button("Large", value="large"),
            Radio.Button("Default", value="default"),
            Radio.Button("Small", value="small"),
        ],
        defaultValue="small",
    )
    autorun(lambda: print(size()))
    return [
        size,
        Button("Primary", type="primary", size=size),
    ]
