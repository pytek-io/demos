from reflect_html import *
from reflect_antd import Input
from reflect import autorun


TextArea = Input.TextArea


def app():
    text_area = TextArea(
        placeholder="Controlled autosize",
        autoSize=dict(minRows=3, maxRows=5),
    )
    autorun(lambda: print("text area value", text_area()))
    return div([
        TextArea(placeholder="Autosize height based on content lines", autoSize=True),
        div(style=dict(margin="24px 0")),
        TextArea(
            placeholder="Autosize height with minimum and maximum number of lines",
            autoSize=dict(minRows=2, maxRows=6),
        ),
        div(style=dict(margin="24px 0")),
        text_area,
    ])
