from render_ant_icons import AudioOutlined
from render_antd import Input, Space
from render_html import *

Search = Input.Search


def app():
    suffix = AudioOutlined(style={"fontSize": 16, "color": "#1890ff"})
    onSearch = lambda v: print("searching", v)
    return Space(
        [
            Search(
                placeholder="input search text", onSearch=onSearch, style={"width": 200}
            ),
            Search(
                placeholder="input search text",
                allowClear=True,
                onSearch=onSearch,
                style={"width": 200},
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
