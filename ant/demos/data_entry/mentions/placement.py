import reflect_antd as antd
import reflect_html as html

Option = antd.Mentions.Option


def app():
    return antd.Mentions(
        options=[
            {"label": "afc163", "value": "afc163"},
            {"label": "zombieJ", "value": "zombieJ"},
            {"label": "yesmeck", "value": "yesmeck"},
        ],
        style=dict(width="100%"),
        placement="top",
    )
