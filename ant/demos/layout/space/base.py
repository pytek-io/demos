from reflect_html import *
from reflect_antd import Button, Space, Upload, Popconfirm
from reflect_ant_icons import UploadOutlined


def app():
    return Space(
        [
            "Space",
            Button("Button", type="primary"),
            Upload(Button([UploadOutlined(), "Click to Upload"])),
            Popconfirm(
                Button("Confirm"),
                title="Are you sure delete this task?",
                okText="Yes",
                cancelText="No",
            ),
        ]
    )
