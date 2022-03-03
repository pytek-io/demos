import random

from reflect import make_observable
from reflect_ant_icons import MinusOutlined, PlusOutlined, QuestionOutlined
from reflect_antd import Badge, Button, Switch
from reflect_html import *
from reflect_utils.misc import increment_observable_bounded

MIN_VALUE = 0
MAX_VALUE = 1000


def app():
    count = make_observable(5)
    show = Switch(defaultChecked=True)
    return div(
        [
            div(
                [
                    Badge(a(href="#", className="head-example"), count=count),
                    Button.Group(
                        [
                            Button(
                                MinusOutlined(),
                                onClick=increment_observable_bounded(
                                    count, MIN_VALUE, MAX_VALUE, -1
                                ),
                            ),
                            Button(
                                PlusOutlined(),
                                onClick=increment_observable_bounded(
                                    count, MIN_VALUE, MAX_VALUE, 1
                                ),
                            ),
                            Button(
                                QuestionOutlined(),
                                onClick=lambda: count.set(
                                    random.randint(MIN_VALUE, MAX_VALUE)
                                ),
                            ),
                        ]
                    ),
                ],
            ),
            br(),
            div(
                [
                    Badge(a(href="#", className="head-example"), dot=show),
                    show,
                ],
            ),
        ],
    )
