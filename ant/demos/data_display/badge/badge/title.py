import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Badge(
                html.a(href="#", className="head-example"),
                count=5,
                title="Custom hover text",
            ),
            antd.Badge(
                html.a(href="#", className="head-example"), count=-5, title="Negative"
            ),
        ]
    )
