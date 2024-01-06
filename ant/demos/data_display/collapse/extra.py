import render as r
import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def genExtra():
    # not sure why we would want to set stop_propagation to True
    return ant_icons.SettingOutlined(onClick=r.Callback(stop_propagation=True))


def app():
    text = """
A dog is a type of domesticated animal.
Known for its loyalty and faithfulness,
it can be found as a welcome guest in many households across the world.
"""
    expandIconPosition = antd.Select(
        options=[
            {"title": "Start", "value": "start"},
            {"title": "End", "value": "end"},
        ],
        defaultValue="start",
        style={"margin": "0 8px"},
    )
    return html.div(
        [
            antd.Collapse(
                [
                    antd.Collapse.Panel(
                        html.div(text),
                        header="This is panel header 1",
                        key="1",
                        extra=genExtra(),
                    ),
                    antd.Collapse.Panel(
                        html.div(text),
                        header="This is panel header 2",
                        key="2",
                        extra=genExtra(),
                    ),
                    antd.Collapse.Panel(
                        html.div(text),
                        header="This is panel header 3",
                        key="3",
                        extra=genExtra(),
                    ),
                ],
                defaultActiveKey=["1"],
                onChange=print,
                expandIconPosition=expandIconPosition,
            ),
            html.br(),
            html.span("Expand Icon Position:"),
            expandIconPosition,
        ]
    )
