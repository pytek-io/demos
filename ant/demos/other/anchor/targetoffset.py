from reflect_html import *
from reflect_antd import Anchor

Link = Anchor.Link


def app():
    raise NotImplementedError("useEffect hook not supported yet")
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
        targetOffset=targetOffset,
    )
