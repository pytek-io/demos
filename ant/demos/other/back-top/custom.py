from reflect_html import *
from reflect_antd import BackTop

style = dict(
    height=40,
    width=40,
    lineHeight="40px",
    borderRadius=4,
    backgroundColor="#1088e9",
    color="#fff",
    textAlign="center",
    fontSize=14,
)


def app():
    return div(
        [
            div("Scroll to bottom"),
            div("Scroll to bottom"),
            div("Scroll to bottom"),
            div("Scroll to bottom"),
            div("Scroll to bottom"),
            div("Scroll to bottom"),
            div("Scroll to bottom"),
            BackTop(div("UP", style=style)),
        ],
        style=dict(height="600vh", padding=8),
    )
