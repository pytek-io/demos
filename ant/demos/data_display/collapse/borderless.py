from reflect_html import *
from reflect_antd import Collapse

Panel = Collapse.Panel


def app():
    text = p(
        "A dog is a type of domesticated animal. Known for its loyalty and faithfulness, it can be found     as a welcome guest in many households across the world.",
        style=dict(paddingLeft=24),
    )
    return Collapse(
        [
            Panel(text, header="This is panel header 1", key="1"),
            Panel(text, header="This is panel header 2", key="2"),
            Panel(text, header="This is panel header 3", key="3"),
        ],
        bordered=False,
        defaultActiveKey=["1"],
    )
