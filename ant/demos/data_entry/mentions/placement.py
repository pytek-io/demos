import render_antd as antd
import render_html as html


def app(_):
    return antd.Mentions(
        options=[
            {"label": "afc163", "value": "afc163"},
            {"label": "zombieJ", "value": "zombieJ"},
            {"label": "yesmeck", "value": "yesmeck"},
        ],
        style={"width": "100%"},
        placement="top",
    )
