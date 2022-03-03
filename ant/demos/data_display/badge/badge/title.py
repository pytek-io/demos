from reflect_html import *
from reflect_antd import Badge


def app():
    return div(
        [
            Badge(
                a(href="#", className="head-example"),
                count=5,
                title="Custom hover text",
            ),
            Badge(a(href="#", className="head-example"), count=-5, title="Negative"),
        ]
    )
