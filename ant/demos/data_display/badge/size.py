import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Badge(
                html.a(href="#", className="head-example"), size="default", count=5
            ),
            antd.Badge(
                html.a(href="#", className="head-example"), size="small", count=5
            ),
        ]
    )
