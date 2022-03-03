from reflect_html import *
from reflect_antd import Anchor
from reflect import js

Link = Anchor.Link


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
        getCurrentAnchor=js("constant", "#components-anchor-demo-static"),
    )
