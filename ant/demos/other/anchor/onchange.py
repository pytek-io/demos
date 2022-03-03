from reflect_html import *
from reflect_antd import Anchor
from reflect import Callback

Link = Anchor.Link


def onChange(link):
    print("Anchor:OnChange", link)


def app():
    return Anchor(
        [
            Link(href="#components-anchor-demo-basic", title="Basic demo"),
            Link(href="#components-anchor-demo-static", title="Static demo"),
            Link(
                [
                    Link(href="#Anchor-Props", title="Anchor Props"),
                    Link(href="#Link-Props", title="Link Props"),
                ],
                href="#API",
                title="API",
            ),
        ],
        affix=False,
        onChange=Callback(onChange),
    )
