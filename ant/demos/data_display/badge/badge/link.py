import reflect_antd as antd
import reflect_html as html


def app():
    return html.a(antd.Badge(html.span(className="head-example"), count=5), href="#")
