import reflect as r
import reflect_antd as antd


def app():
    select = antd.Select(
        options=[
            {
                "label": [
                    {"label": "Jack", "value": "jack"},
                    {"label": "Lucy", "value": "lucy"},
                ],
                "label": "Manager",
            },
            {"label": {"label": "yiminghe", "value": "Yiminghe"}, "label": "Engineer"},
        ],
        defaultValue="lucy",
        style=dict(width=200),
    )
    r.autorun(lambda: print(select()))
    return select
