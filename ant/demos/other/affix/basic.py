from functools import partial

import render as r
import render_antd as antd
import render_html as html


def app():
    top = r.ObservableValue(10)
    bottom = r.ObservableValue(10)
    return html.div(
        [
            antd.Affix(
                antd.Button(
                    "Affix top", type="primary", onClick=partial(top.__iadd__, 10)
                ),
                offsetTop=top,
            ),
            html.br(),
            antd.Affix(
                antd.Button(
                    "Affix bottom", type="primary", onClick=partial(bottom.__iadd__, 10)
                ),
                offsetBottom=bottom,
            ),
        ]
    )
