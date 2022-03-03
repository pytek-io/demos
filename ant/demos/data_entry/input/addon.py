from reflect_html import *
from reflect_antd import Input, Select
from reflect_ant_icons import SettingOutlined

Option = Select.Option
selectBefore = Select(
    [Option("http://", value="http://"), Option("https://", value="https://")],
    defaultValue="http://",
    className="select-before",
)
selectAfter = Select(
    [
        Option(".com", value=".com"),
        Option(".jp", value=".jp"),
        Option(".cn", value=".cn"),
        Option(".org", value=".org"),
    ],
    defaultValue=".com",
    className="select-after",
)


def app():
    return [
        div(
            Input(addonBefore="http://", addonAfter=".com", defaultValue="mysite"),
            style=dict(marginBottom=16),
        ),
        div(
            Input(
                addonBefore=selectBefore, addonAfter=selectAfter, defaultValue="mysite"
            ),
            style=dict(marginBottom=16),
        ),
        div(
            Input(addonAfter=SettingOutlined([]), defaultValue="mysite"),
            style=dict(marginBottom=16),
        ),
        div(
            Input(addonBefore="http://", suffix=".com", defaultValue="mysite"),
            style=dict(marginBottom=16),
        ),
    ]
