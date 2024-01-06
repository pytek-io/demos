import render as r
import render_antd as antd

def app():
    mentions = antd.Mentions(
        options=[
            {"label": "afc163", "value": "afc163", "key": 0},
            {"label": "zombieJ", "value": "zombieJ", "key": 1},
            {"label": "yesmeck", "value": "yesmeck", "key": 2},
        ],
        style={"width": "100%"},
        defaultValue="@afc163",
    )
    r.autoprint(mentions)
    return mentions
