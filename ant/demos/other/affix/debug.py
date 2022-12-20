import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    top = r.create_observable(10, key="test")
    return html.div(
        [
            html.div("Top"),
            antd.Affix(
                html.div(
                    antd.Button(
                        "Affix top", type="primary", onClick=lambda: top.set(top() + 10)
                    ),
                    style=dict(background="red"),
                ),
                offsetTop=top,
            ),
            html.div("Bottom"),
        ],
        style=dict(height=10000),
    )