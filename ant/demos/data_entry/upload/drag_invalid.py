from render_ant_icons import InboxOutlined
from render_antd import Upload, message
from render_html import *

Dragger = Upload.Dragger


def app():
    return Dragger(
        [
            p(InboxOutlined(), className="ant-upload-drag-icon"),
            p("Click or drag file to this area to upload", className="ant-upload-text"),
            p(
                "Support for a single or bulk upload. Strictly prohibit from uploading company data or other       band files",
                className="ant-upload-hint",
            ),
        ],
    )
