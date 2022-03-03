from reflect_html import *
from reflect_antd import Collapse
from reflect import js
Panel = Collapse.Panel


def app():
    text = """
A dog is a type of domesticated animal.
Known for its loyalty and faithfulness,
it can be found as a welcome guest in many households across the world.
"""
    return Collapse(
        [
            Panel(
                p(text),
                header="This is panel header 1",
                key="1",
                className="site-collapse-custom-panel",
            ),
            Panel(
                p(text),
                header="This is panel header 2",
                key="2",
                className="site-collapse-custom-panel",
            ),
            Panel(
                p(text),
                header="This is panel header 3",
                key="3",
                className="site-collapse-custom-panel",
            ),
        ],
        bordered=False,
        defaultActiveKey=["1"],
        expandIcon=js("collapseExpandIcon"),
    )
