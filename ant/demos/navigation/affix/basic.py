from reflect_html import *
from reflect_antd import Affix, Button
from reflect import make_observable


def increment(value, increment):
    def result():
        nonlocal value
        value += increment

    return result


def app():
    top = make_observable(10)
    bottom = make_observable(10)

    return [
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
