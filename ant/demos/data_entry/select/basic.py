import render as r
import render_antd as antd
import render_html as html


def app(_):
    select = antd.Select(
        options=[
            {"label": "Jack", "value": "jack"},
            {"label": "Lucy", "value": "lucy"},
            {"label": "Disabled", "value": "disabled", "disabled": True},
            {"label": "yiminghe", "value": "Yiminghe"},
        ],
        defaultValue="lucy",
        style={"width": 120},
    )
    r.autorun(lambda: print("selected", select()))
    return html.div(
        [
            select,
            antd.Select(
                options=[{"label": "Lucy", "value": "lucy"}],
                defaultValue="lucy",
                style={"width": 120},
                disabled=True,
            ),
            antd.Select(
                options=[{"label": "Lucy", "value": "lucy"}],
                defaultValue="lucy",
                style={"width": 120},
                loading=True,
            ),
            antd.Select(
                options=[{"label": "Lucy", "value": "lucy"}],
                defaultValue="lucy",
                style={"width": 120},
                allowClear=True,
            ),
        ]
    )
