import traceback

import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    counters = [r.create_observable(value) for value in [1, 2]]

    def update_counters(value):
        counters[value] += 1

    result = antd.Radio.Group(
        [
            antd.Badge(
                antd.Radio.Button("Click Me", value=0), count=lambda: counters[0]
            ),
            antd.Badge(antd.Radio.Button("Not Me", value=1), count=lambda: counters[1]),
        ],
        buttonStyle="solid",
        onChange=update_counters,
    )
    r.autorun(lambda: print(result()))
    return result
