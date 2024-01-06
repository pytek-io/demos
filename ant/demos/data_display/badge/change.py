import random

import render as r
import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html
import render_utils

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
                                onClick=render_utils.increment_observable_bounded(
                                    count, MIN_VALUE, MAX_VALUE, -1
                                ),
                            ),
                            antd.Button(
                                ant_icons.PlusOutlined(),
                                onClick=render_utils.increment_observable_bounded(
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
