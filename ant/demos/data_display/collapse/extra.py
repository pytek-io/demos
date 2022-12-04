import reflect as r
import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

Panel = antd.Collapse.Panel
Option = antd.Select.Option


def genExtra():
    return ant_icons.SettingOutlined(onClick=r.Callback(stop_propagation=True))


def app():
    text = """
A dog is a type of domesticated animal.
Known for its loyalty and faithfulness,
it can be found as a welcome guest in many households across the world.
"""
    expandIconPosition = antd.Select(
        [Option("left", value="left"), Option("right", value="right")],
        defaultValue="left",
        style=dict(margin="0 8px"),
    )
    return html.div(
        [
            antd.Collapse(
                [
                    Panel(
                        html.div(text),
                        header="This is panel header 1",
                        key="1",
                        extra=genExtra(),
                    ),
                    Panel(
                        html.div(text),
                        header="This is panel header 2",
                        key="2",
                        extra=genExtra(),
                    ),
                    Panel(
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
