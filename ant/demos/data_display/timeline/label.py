import render_antd as antd
import render_html as html


def app(_):
    mode = antd.Radio.Group(
        [
            antd.Radio("Left", value="left"),
            antd.Radio("Right", value="right"),
            antd.Radio("Alternate", value="alternate"),
        ],
        defaultValue="left",
        style={"marginBottom": 20},
    )
    return html.div(
        [
            mode,
            antd.Timeline(
                items=[
                    {
                        "label": "2015-09-01",
                        "children": "Create a services",
                    },
                    {
                        "label": "2015-09-01 09:12:11",
                        "children": "Solve initial network problems",
                    },
                    {
                        "children": "Technical testing",
                    },
                    {
                        "label": "2015-09-01 09:12:11",
                        "children": "Network problems being solved",
                    },
                ],
                mode=mode,
            ),
        ]
    )
