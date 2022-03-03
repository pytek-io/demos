from reflect_html import *
from reflect_antd import Timeline, Radio


def app():
    mode = Radio.Group(
        [
            Radio("Left", value="left"),
            Radio("Right", value="right"),
            Radio("Alternate", value="alternate"),
        ],
        defaultValue="left",
        style=dict(marginBottom=20),
    )
    return [
        mode,
        Timeline(
            [
                Timeline.Item("Create a services", label="2015-09-01"),
                Timeline.Item(
                    "Solve initial network problems", label="2015-09-01 09:12:11"
                ),
                Timeline.Item("Technical testing"),
                Timeline.Item(
                    "Network problems being solved", label="2015-09-01 09:12:11"
                ),
            ],
            mode=mode,
        ),
    ]
