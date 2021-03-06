from reflect_html import *
from reflect_antd import Input, Space
from reflect_ant_icons import AudioOutlined
from reflect import Callback
Search = Input.Search


def app():
    suffix = AudioOutlined(style=dict(fontSize=16, color="#1890ff"))
    onSearch = Callback(lambda v: print(v))
    return Space(
        [
            Search(
                placeholder="input search text",
                onSearch=onSearch,
                style=dict(width=200),
            ),
            Search(
                placeholder="input search text",
                allowClear=True,
                onSearch=onSearch,
                style=dict(width=200),
            ),
            Search(
                placeholder="input search text", onSearch=onSearch, enterButton=True
            ),
            Search(
                placeholder="input search text",
                allowClear=True,
                enterButton="Search",
                size="large",
                onSearch=onSearch,
            ),
            Search(
                placeholder="input search text",
                enterButton="Search",
                size="large",
                suffix=suffix,
                onSearch=onSearch,
            ),
        ],
        direction="vertical",
    )
