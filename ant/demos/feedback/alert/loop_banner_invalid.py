from render_html import *
from render_antd import Alert


def app():
    raise NotImplementedError("react-text-lopp not exposed")
    return Alert(
        banner=True,
        message=TextLoop(
            [
                div("Notice message one"),
                div("Notice message two"),
                div("Notice message three"),
                div("Notice message four"),
            ], mask=True
        ),
    )
