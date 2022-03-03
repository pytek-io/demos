from reflect_html import *
from reflect_antd import Timeline


def app():
    return Timeline(
        [
            Timeline.Item("Create a services site 2015-09-01", color="green"),
            Timeline.Item("Create a services site 2015-09-01", color="green"),
            Timeline.Item(
                [
                    p("Solve initial network problems 1"),
                    p("Solve initial network problems 2"),
                    p("Solve initial network problems 3 2015-09-01"),
                ],
                color="red",
            ),
            Timeline.Item(
                [
                    p("Technical testing 1"),
                    p("Technical testing 2"),
                    p("Technical testing 3 2015-09-01"),
                ]
            ),
            Timeline.Item(
                [
                    p("Technical testing 1"),
                    p("Technical testing 2"),
                    p("Technical testing 3 2015-09-01"),
                ],
                color="gray",
            ),
            Timeline.Item(
                [
                    p("Technical testing 1"),
                    p("Technical testing 2"),
                    p("Technical testing 3 2015-09-01"),
                ],
                color="gray",
            ),
        ]
    )
