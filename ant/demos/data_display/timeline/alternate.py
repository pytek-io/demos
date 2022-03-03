from reflect_html import *
from reflect_antd import Timeline
from reflect_ant_icons import ClockCircleOutlined


def app():
    return Timeline(
        [
            Timeline.Item("Create a services site 2015-09-01"),
            Timeline.Item("Solve initial network problems 2015-09-01", color="green"),
            Timeline.Item(
                "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque       laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto       beatae vitae dicta sunt explicabo.",
                dot=ClockCircleOutlined(style={"fontSize": "16px"}),
            ),
            Timeline.Item("Network problems being solved 2015-09-01", color="red"),
            Timeline.Item("Create a services site 2015-09-01"),
            Timeline.Item(
                "Technical testing 2015-09-01",
                dot=ClockCircleOutlined(style={"fontSize": "16px"}),
            ),
        ],
        mode="alternate",
    )
