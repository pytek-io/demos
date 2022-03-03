from reflect_html import *
from reflect_antd import Collapse, Select
from reflect_ant_icons import SettingOutlined
from reflect import js, Callback

Panel = Collapse.Panel
Option = Select.Option


def genExtra():
    return SettingOutlined(onClick=Callback(stop_propagation=True))


def app():
    text = """
A dog is a type of domesticated animal.
Known for its loyalty and faithfulness,
it can be found as a welcome guest in many households across the world.
"""
    expandIconPosition = Select(
        [Option("left", value="left"), Option("right", value="right")],
        defaultValue="left",
        style=dict(margin="0 8px"),
    )
    return div([
        Collapse(
            [
                Panel(
                    div(text),
                    header="This is panel header 1",
                    key="1",
                    extra=genExtra(),
                ),
                Panel(
                    div(text),
                    header="This is panel header 2",
                    key="2",
                    extra=genExtra(),
                ),
                Panel(
                    div(text),
                    header="This is panel header 3",
                    key="3",
                    extra=genExtra(),
                ),
            ],
            defaultActiveKey=["1"],
            onChange=print,
            expandIconPosition=expandIconPosition,
        ),
        br(),
        span("Expand Icon Position:"),
        expandIconPosition,
    ])
