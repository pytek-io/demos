from reflect_html import *
from reflect_antd import Affix, Button
from reflect import create_observable


def increment(value, increment):
    def result():
        nonlocal value
        value += increment

    return result


def app():
    top = create_observable(10)
    bottom = create_observable(10)

    return div(
        [
            Affix(
                Button("Affix top", type="primary", onClick=increment(top, 10)),
                offsetTop=top,
            ),
            br(),
            Affix(
                Button(
                    "Affix bottom",
                    type="primary",
                    onClick=increment(bottom, 10),
                ),
                offsetBottom=bottom,
            ),
        ]
    )
