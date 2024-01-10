import render_antd as antd
import render_html as html


def app(_):
    mode = antd.Radio.Group(
        [
            antd.Radio.Button("Horizontal", value="top"),
            antd.Radio.Button("Vertical", value="left"),
        ],
        defaultValue="top",
        style={"marginBottom": 8},
    )
    return html.div(
        [
            mode,
            antd.Tabs(
                items=[
                    {
                        "children": f"Content of tab {i}",
                        "label": f"Tab-{i}",
                        "key": i,
                        "disabled": i == 28,
                    }
                    for i in range(1, 30)
                ],
                defaultActiveKey="3",
                tabPosition=mode,
                style={"height": 220},
            ),
        ]
    )
