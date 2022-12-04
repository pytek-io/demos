import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Timeline(
        [
            antd.Timeline.Item("Create a services site 2015-09-01", color="green"),
            antd.Timeline.Item("Create a services site 2015-09-01", color="green"),
            antd.Timeline.Item(
                [
                    html.p("Solve initial network problems 1"),
                    html.p("Solve initial network problems 2"),
                    html.p("Solve initial network problems 3 2015-09-01"),
                ],
                color="red",
            ),
            antd.Timeline.Item(
                [
                    html.p("Technical testing 1"),
                    html.p("Technical testing 2"),
                    html.p("Technical testing 3 2015-09-01"),
                ]
            ),
            antd.Timeline.Item(
                [
                    html.p("Technical testing 1"),
                    html.p("Technical testing 2"),
                    html.p("Technical testing 3 2015-09-01"),
                ],
                color="gray",
            ),
            antd.Timeline.Item(
                [
                    html.p("Technical testing 1"),
                    html.p("Technical testing 2"),
                    html.p("Technical testing 3 2015-09-01"),
                ],
                color="gray",
            ),
        ]
    )
