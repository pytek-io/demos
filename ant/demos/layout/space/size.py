from reflect_html import *
from reflect_antd import Space, Radio, Button


def app():

    size = Radio.Group(
        [
            Radio("Small", value="small"),
            Radio("Middle", value="middle"),
            Radio("Large", value="large"),
        ],
        defaultValue="small",
    )
    return div(
        [
            size,
            br(),
            br(),
            Space(
                [
                    Button("Primary", type="primary"),
                    Button("Default"),
                    Button("Dashed", type="dashed"),
                    Button("Link", type="link"),
                ],
                size=size,
            ),
        ]
    )
