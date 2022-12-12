import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

import reflect as r


def app():
    smileIcon = ant_icons.SmileOutlined()
    mehIcon = ant_icons.MehOutlined()
    select = antd.Select(
        options=[
            {"label": "Jack", "value": "jack"},
            {"label": "Lucy", "value": "lucy"},
            {"label": "Disabled", "value": "disabled", "disabled": True},
            {"label": "yiminghe", "value": "Yiminghe"},
        ],
        suffixIcon=smileIcon,
        defaultValue="lucy",
        style=dict(width=120),
    )
    r.autorun(lambda: print("selected", select()))
    return html.div(
        [
            select,
            antd.Select(
                options=[{"label": "Lucy", "value": "lucy"}],
                suffixIcon=mehIcon,
                defaultValue="lucy",
                style=dict(width=120),
                disabled=True,
            ),
        ]
    )
