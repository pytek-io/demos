import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Badge(
        html.a(href="#", className="head-example"), count=5, offset=[10, 10]
    )
