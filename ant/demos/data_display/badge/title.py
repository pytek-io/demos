import render_antd as antd
import render_html as html


def app(_):
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
