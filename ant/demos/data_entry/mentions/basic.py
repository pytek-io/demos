import reflect as r
import reflect_antd as antd


def onSelect(value):
    print("selected", value)


def app():
    mentions = antd.Mentions(
        options=[
            {"label": "afc163", "value": "afc163"},
            {"label": "zombieJ", "value": "zombieJ"},
            {"label": "yesmeck", "value": "yesmeck"},
        ],
        style={"width": "100%"},
        onSelect=r.Callback(onSelect),
        defaultValue="@afc163",
    )
    r.autorun(lambda: print(mentions()))
    return mentions
