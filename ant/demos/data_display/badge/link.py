import render_antd as antd
import render_html as html


def app(_):
    return html.a(antd.Badge(html.span(className="head-example"), count=5), href="#")
