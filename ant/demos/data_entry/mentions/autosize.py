from reflect_html import *
from reflect_antd import Mentions

Option = Mentions.Option


def app():
    return Mentions(
        [
            Option("afc163", value="afc163"),
            Option("zombieJ", value="zombieJ"),
            Option("yesmeck", value="yesmeck"),
        ],
        autoSize=True,
        style=dict(width="100%"),
    )
