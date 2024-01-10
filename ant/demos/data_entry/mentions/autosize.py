import render_antd as antd


def app(_):
    return antd.Mentions(
        options=[
            {"label": "afc163", "value": "afc163", "key": 0},
            {"label": "zombieJ", "value": "zombieJ", "key": 1},
            {"label": "yesmeck", "value": "yesmeck", "key": 2},
        ],
        autoSize=True,
        style={"width": "100%"},
    )
