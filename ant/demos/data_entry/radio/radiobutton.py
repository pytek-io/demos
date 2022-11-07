from reflect_html import *
from reflect_antd import Radio



def onChange(value):
    print(f"radio checked:{value}")


def app():
    return div([
        Radio.Group(
            [
                Radio.Button("Hangzhou", value="a"),
                Radio.Button("Shanghai", value="b"),
                Radio.Button("Beijing", value="c"),
                Radio.Button("Chengdu", value="d"),
            ],
            onChange=onChange,
            defaultValue="a",
        ),
        Radio.Group(
            [
                Radio.Button("Hangzhou", value="a"),
                Radio.Button("Shanghai", value="b", disabled=True),
                Radio.Button("Beijing", value="c"),
                Radio.Button("Chengdu", value="d"),
            ],
            onChange=onChange,
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
            disabled=True,
            onChange=onChange,
            defaultValue="a",
            style=dict(marginTop=16),
        ),
    ]
)