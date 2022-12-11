import reflect_antd as antd
import reflect_html as html

import reflect as r

Option, OptGroup = antd.Select.Option, antd.Select.OptGroup


def app():
    select = antd.Select(
        options=[
            OptGroup(
                [
                    {"label": "Jack", "value": "jack"},
                    {"label": "Lucy", "value": "lucy"},
                ],
                label="Manager",
            ),
            OptGroup({"label": "yiminghe", "value": "Yiminghe"}, label="Engineer"),
        ],
        defaultValue="lucy",
        style=dict(width=200),
    )
    r.autorun(lambda: print(select()))
    return select
