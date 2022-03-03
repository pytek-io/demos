from reflect_html import *
from reflect_antd import Upload, Button, Space
from reflect_ant_icons import UploadOutlined


def app():
    return Space(
        [
            Upload(
                Button("Upload (Max: 1)", icon=UploadOutlined([])),
                action="https://www.mocky.io/v2/5cc8019d300000980a055e76",
                listType="picture",
                maxCount=1,
            ),
            Upload(
                Button("Upload (Max: 3)", icon=UploadOutlined([])),
                action="https://www.mocky.io/v2/5cc8019d300000980a055e76",
                listType="picture",
                maxCount=3,
                multiple=True,
            ),
        ],
        direction="vertical",
        style=dict(width="100%"),
        size="large",
    )
