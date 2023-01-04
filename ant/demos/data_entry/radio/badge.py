import reflect as r
import reflect_antd as antd


def app():
    counters = [r.ObservableValue(value) for value in [1, 2]]

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
    r.autoprint(result)
    return result
