from render_antd import Collapse
from render_html import *

Panel = Collapse.Panel


def app(_):
    return Collapse(
        [
            Panel(p(text), header="This is panel header with arrow icon", key="1"),
            Panel(
                p(text),
                showArrow=False,
                header="This is panel header with no arrow icon",
                key="2",
            ),
        ],
        defaultActiveKey=["1"],
        onChange=callback,
    )
