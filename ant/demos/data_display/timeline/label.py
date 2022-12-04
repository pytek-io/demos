import reflect_antd as antd
import reflect_html as html


def app():
    mode = antd.Radio.Group(
        [
            antd.Radio("Left", value="left"),
            antd.Radio("Right", value="right"),
            antd.Radio("Alternate", value="alternate"),
        ],
        defaultValue="left",
        style=dict(marginBottom=20),
    )
    return html.div(
        [
            mode,
            antd.Timeline(
                [
                    antd.Timeline.Item("Create a services", label="2015-09-01"),
                    antd.Timeline.Item(
                        "Solve initial network problems", label="2015-09-01 09:12:11"
                    ),
                    antd.Timeline.Item("Technical testing"),
                    antd.Timeline.Item(
                        "Network problems being solved", label="2015-09-01 09:12:11"
                    ),
                ],
                mode=mode,
            ),
        ]
    )
