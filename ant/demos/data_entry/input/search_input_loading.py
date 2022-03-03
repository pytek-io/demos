from reflect_html import *
from reflect_antd import Input

Search = Input.Search


def app():
    return [
        Search(placeholder="input search loading default", loading=True),
        br(),
        br(),
        Search(
            placeholder="input search loading with enterButton",
            loading=True,
            enterButton=True,
        ),
        br(),
        br(),
        Search(
            placeholder="input search text",
            enterButton="Search",
            size="large",
            loading=True,
        ),
    ]
