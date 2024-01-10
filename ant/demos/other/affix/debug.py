import render as r
import render_antd as antd
import render_html as html


def app(_):
    top = r.ObservableValue(10, key="test")
    return html.div(
        [
            html.div("Top"),
            antd.Affix(
                html.div(
                    antd.Button(
                        "Affix top", type="primary", onClick=lambda: top.set(top() + 10)
                    ),
                    style={"background": "red"},
                ),
                offsetTop=top,
            ),
            html.div("Bottom"),
        ],
        style={"height": 10000},
    )
