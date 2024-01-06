import render as r
import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


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
        style={"width": 120},
    )
    r.autorun(lambda: print("selected", select()))
    return html.div(
        [
            select,
            antd.Select(
                options=[{"label": "Lucy", "value": "lucy"}],
                suffixIcon=mehIcon,
                defaultValue="lucy",
                style={"width": 120},
                disabled=True,
            ),
        ]
    )
