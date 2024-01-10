import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Select(
                options=[
                    {"label": "Jack", "value": "jack"},
                    {"label": "Lucy", "value": "lucy"},
                    {"label": "yiminghe", "value": "Yiminghe"},
                ],
                defaultValue="lucy",
                style={"width": 120},
                bordered=False,
            ),
            antd.Select(
                options=[{"label": "Lucy", "value": "lucy"}],
                defaultValue="lucy",
                style={"width": 120},
                disabled=True,
                bordered=False,
            ),
        ]
    )
