import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Mentions(
        options=[
            {"label": "afc163", "value": "afc163"},
            {"label": "zombieJ", "value": "zombieJ"},
            {"label": "yesmeck", "value": "yesmeck"},
        ],
        style={"width": "100%"},
        placement="top",
    )
