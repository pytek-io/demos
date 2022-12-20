import reflect_antd as antd


def app():
    return antd.Mentions(
        options=[
            {"label": "afc163", "value": "afc163"},
            {"label": "zombieJ", "value": "zombieJ"},
            {"label": "yesmeck", "value": "yesmeck"},
        ],
        autoSize=True,
        style=dict(width="100%"),
    )
