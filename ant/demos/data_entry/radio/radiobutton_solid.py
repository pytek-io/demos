from reflect_html import *
from reflect_antd import Radio


def app():
    return [
        Radio.Group(
            [
                Radio.Button("Hangzhou", value="a"),
                Radio.Button("Shanghai", value="b"),
                Radio.Button("Beijing", value="c"),
                Radio.Button("Chengdu", value="d"),
            ],
            defaultValue="a",
            buttonStyle="solid",
        ),
        Radio.Group(
            [
                Radio.Button("Hangzhou", value="a"),
                Radio.Button("Shanghai", value="b", disabled=True),
                Radio.Button("Beijing", value="c"),
                Radio.Button("Chengdu", value="d"),
            ],
            defaultValue="c",
            buttonStyle="solid",
            style=dict(marginTop=16),
        ),
    ]
