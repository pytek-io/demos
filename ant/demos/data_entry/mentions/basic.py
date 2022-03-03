from reflect_html import *
from reflect_antd import Mentions
from reflect import Callback
from reflect import autorun

Option = Mentions.Option

def onSelect(value):
    print("selected", value)

def app():
    mentions = Mentions(
        [
            Option("afc163", value="afc163"),
            Option("zombieJ", value="zombieJ"),
            Option("yesmeck", value="yesmeck"),
        ],
        style=dict(width="100%"),
        onSelect=Callback(onSelect),
        defaultValue="@afc163",
    )
    autorun(lambda: print(mentions()))
    return mentions