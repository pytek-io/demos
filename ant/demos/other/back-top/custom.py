import reflect_antd as antd
import reflect_html as html

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
    return html.div(
        [
            html.div("Scroll to bottom"),
            html.div("Scroll to bottom"),
            html.div("Scroll to bottom"),
            html.div("Scroll to bottom"),
            html.div("Scroll to bottom"),
            html.div("Scroll to bottom"),
            html.div("Scroll to bottom"),
            antd.BackTop(html.div("UP", style=style)),
        ],
        style=dict(height="600vh", padding=8),
    )
