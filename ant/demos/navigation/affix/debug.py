from reflect_html import *
from reflect_antd import Affix, Button
from reflect import make_observable


def app():
    top = make_observable(10, key="test")
    return div(
        [
            div("Top"),
            Affix(
                div(
                    Button(
                        "Affix top",
                        type="primary",
                        onClick=lambda: top.set(top() + 10),
                    ),
                    style=dict(background="red"),
                ),
                offsetTop=top,
            ),
            div("Bottom"),
        ],
        style=dict(height=10000),
    )
