import reflect as r
import reflect_antd as antd
import reflect_html as html

Link = antd.Anchor.Link


def onChange(link):
    print("Anchor:OnChange", link)


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
        onChange=r.Callback(onChange),
    )
