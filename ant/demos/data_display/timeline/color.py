import render_antd as antd
import render_ant_icons as ant_icons
import render_html as html


def app():
    return antd.Timeline(
        items=[
            {
                "color": "green",
                "children": "Create a services site 2015-09-01",
            },
            {
                "color": "green",
                "children": "Create a services site 2015-09-01",
            },
            {
                "color": "red",
                "children": [
                    html.p("Solve initial network problems 1"),
                    html.p("Solve initial network problems 2"),
                    html.p("Solve initial network problems 3 2015-09-01"),
                ],
            },
            {
                "children": [
                    html.p("Technical testing 1"),
                    html.p("Technical testing 2"),
                    html.p("Technical testing 3 2015-09-01"),
                ]
            },
            {
                "color": "gray",
                "children": [
                    html.p("Technical testing 1"),
                    html.p("Technical testing 2"),
                    html.p("Technical testing 3 2015-09-01"),
                ],
            },
            {
                "color": "gray",
                "children": [
                    html.p("Technical testing 1"),
                    html.p("Technical testing 2"),
                    html.p("Technical testing 3 2015-09-01"),
                ],
            },
            {
                "color": "#00CCFF",
                "dot": ant_icons.SmileOutlined(),
                "children": html.p(
                    "Custom color testing",
                ),
            },
        ]
    )
