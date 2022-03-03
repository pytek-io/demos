from reflect_html import *
from reflect_antd import Collapse
from reflect import Callback

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
                Collapse(
                    Panel(p(text), header="This is panel nest panel", key="1"),
                    defaultActiveKey="1",
                ),
                header="This is panel header 1",
                key="1",
            ),
            Panel(p(text), header="This is panel header 2", key="2"),
            Panel(p(text), header="This is panel header 3", key="3"),
        ],
        onChange=Callback(lambda key: print(f"{key} clicked")),
    )
