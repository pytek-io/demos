from functools import partial

import reflect_antd as antd
import reflect_html as html

import reflect as r


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
