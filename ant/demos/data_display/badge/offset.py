import render_antd as antd
import render_html as html


def app(_):
    return antd.Badge(
        html.a(href="#", className="head-example"), count=5, offset=[10, 10]
    )
