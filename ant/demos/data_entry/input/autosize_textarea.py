import reflect as r
import reflect_antd as antd
import reflect_html as html

TextArea = antd.Input.TextArea


def app():
    text_area = TextArea(
        placeholder="Controlled autosize", autoSize=dict(minRows=3, maxRows=5)
    )
    r.autorun(lambda: print("text area value", text_area()))
    return html.div(
        [
            TextArea(
                placeholder="Autosize height based on content lines", autoSize=True
            ),
            html.div(style=dict(margin="24px 0")),
            TextArea(
                placeholder="Autosize height with minimum and maximum number of lines",
                autoSize=dict(minRows=2, maxRows=6),
            ),
            html.div(style=dict(margin="24px 0")),
            text_area,
        ]
    )
