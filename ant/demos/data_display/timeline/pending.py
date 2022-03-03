from reflect import make_observable
from reflect_antd import Button, Timeline
from reflect_html import *
from reflect_utils.common import toggle_observable


def app():
    reverse = make_observable(False)
    return div(
        [
            Timeline(
                [
                    Timeline.Item("Create a services site 2015-09-01"),
                    Timeline.Item("Solve initial network problems 2015-09-01"),
                    Timeline.Item("Technical testing 2015-09-01"),
                ],
                pending="Recording...",
                reverse=reverse,
            ),
            Button(
                "Toggle Reverse",
                type="primary",
                style=dict(marginTop=16),
                onClick=toggle_observable(reverse),
            ),
        ]
    )
