import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    select = antd.Select(
        options=[
            {"label": "Jack", "value": "jack"},
            {"label": "Lucy", "value": "lucy"},
            {"label": "Disabled", "value": "disabled", "disabled": True},
            {"label": "yiminghe", "value": "Yiminghe"},
        ],
        defaultValue="lucy",
        style=dict(width=120),
    )
    r.autorun(lambda: print("selected", select()))
    return html.div(
        [
            select,
            antd.Select(
                options=[{"label": "Lucy", "value": "lucy"}],
                defaultValue="lucy",
                style=dict(width=120),
                disabled=True,
            ),
            antd.Select(
                options=[{"label": "Lucy", "value": "lucy"}],
                defaultValue="lucy",
                style=dict(width=120),
                loading=True,
            ),
            antd.Select(
                options=[{"label": "Lucy", "value": "lucy"}],
                defaultValue="lucy",
                style=dict(width=120),
                allowClear=True,
            ),
        ]
    )
