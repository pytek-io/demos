from render_antd import Affix, Button
from render_html import *


def app():
    raise Exception("parent ref not supported yet")
    return [
        div(
            div(
                Affix(
                    Button("Fixed at the top of container", type="primary"),
                    target=lambda: container,
                ),
                className="background",
            ),
            className="scrollable-container",
            ref=setContainer,
        ),
    ]
