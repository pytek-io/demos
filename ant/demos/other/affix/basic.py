import reflect as r
import reflect_antd as antd
import reflect_html as html


def increment(value, increment):
    def result():
        nonlocal value
        value += increment

    return result


def app():
    top = r.create_observable(10)
    bottom = r.create_observable(10)
    return html.div(
        [
            antd.Affix(
                antd.Button("Affix top", type="primary", onClick=increment(top, 10)),
                offsetTop=top,
            ),
            html.br(),
            antd.Affix(
                antd.Button(
                    "Affix bottom", type="primary", onClick=increment(bottom, 10)
                ),
                offsetBottom=bottom,
            ),
        ]
    )
