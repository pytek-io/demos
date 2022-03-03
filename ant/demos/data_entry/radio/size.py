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
            size="large",
        ),
        Radio.Group(
            [
                Radio.Button("Hangzhou", value="a"),
                Radio.Button("Shanghai", value="b"),
                Radio.Button("Beijing", value="c"),
                Radio.Button("Chengdu", value="d"),
            ],
            defaultValue="a",
            style=dict(marginTop=16),
        ),
        Radio.Group(
            [
                Radio.Button("Hangzhou", value="a"),
                Radio.Button("Shanghai", value="b"),
                Radio.Button("Beijing", value="c"),
                Radio.Button("Chengdu", value="d"),
            ],
            defaultValue="a",
            size="small",
            style=dict(marginTop=16),
        ),
    ]
