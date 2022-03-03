from reflect_html import *
from reflect_antd import Timeline
from reflect_ant_icons import ClockCircleOutlined


def app():
    return Timeline(
        [
            Timeline.Item("Create a services site 2015-09-01"),
            Timeline.Item("Solve initial network problems 2015-09-01"),
            Timeline.Item(
                "Technical testing 2015-09-01",
                dot=ClockCircleOutlined(className="timeline-clock-icon"),
                color="red",
            ),
            Timeline.Item("Network problems being solved 2015-09-01"),
        ]
    )
