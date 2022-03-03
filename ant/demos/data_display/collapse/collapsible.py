from reflect_html import *
from reflect_antd import Collapse, Space

Panel = Collapse.Panel


def app():
    text = """
A dog is a type of domesticated animal.
Known for its loyalty and faithfulness,
it can be found as a welcome guest in many households across the world.
"""
    return Space(
        [
            Collapse(
                Panel(
                    p(text),
                    header="This panel can only be collapsed by clicking text",
                    key="1",
                ),
                collapsible="header",
                defaultActiveKey=["1"],
            ),
            Collapse(
                Panel(p(text), header="This panel can't be collapsed", key="1"),
                collapsible="disabled",
            ),
        ],
        direction="vertical",
    )
