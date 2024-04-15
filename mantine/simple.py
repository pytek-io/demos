import render as r
import render_antd as antd
import render_html as html

def app(_):
    # return html.pre("hello")
    value = r.ObservableValue(0, key="value")

    def increment(increment):
        nonlocal value
        value.set(value() + increment)

    return antd.Space(
        [
            antd.Button("+", onClick=lambda: increment(1)),
            antd.Button("-", onClick=lambda: increment(-1)),
            antd.Badge(count=value),
        ]
    )
