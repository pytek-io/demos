import reflect as r
import reflect_antd as antd

Link = antd.Anchor.Link

getCurrentAnchor = r.js_arrow(
    "getCurrentAnchor", "() => '#components-anchor-demo-static'"
)


def app():
    return antd.Anchor(
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
        getCurrentAnchor=getCurrentAnchor,
    )
