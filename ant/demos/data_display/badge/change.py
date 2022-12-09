import random

import reflect as r
import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html
import reflect_utils

MIN_VALUE = 0
MAX_VALUE = 1000


def app():
    count = r.ObservableValue(5)
    show = antd.Switch(defaultChecked=True)
    return html.div(
        [
            html.div(
                [
                    antd.Badge(html.a(href="#", className="head-example"), count=count),
                    antd.Button.Group(
                        [
                            antd.Button(
                                ant_icons.MinusOutlined(),
                                onClick=reflect_utils.increment_observable_bounded(
                                    count, MIN_VALUE, MAX_VALUE, -1
                                ),
                            ),
                            antd.Button(
                                ant_icons.PlusOutlined(),
                                onClick=reflect_utils.increment_observable_bounded(
                                    count, MIN_VALUE, MAX_VALUE, 1
                                ),
                            ),
                            antd.Button(
                                ant_icons.QuestionOutlined(),
                                onClick=lambda: count.set(
                                    random.randint(MIN_VALUE, MAX_VALUE)
                                ),
                            ),
                        ]
                    ),
                ]
            ),
            html.br(),
            html.div(
                [antd.Badge(html.a(href="#", className="head-example"), dot=show), show]
            ),
        ]
    )
