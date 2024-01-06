import render_antd as antd
import render_html as html


def app():
    return antd.Space(
        [
            antd.Badge(html.a(href="#", className="head-example"), count=99),
            antd.Badge(html.a(href="#", className="head-example"), count=100),
            antd.Badge(
                html.a(href="#", className="head-example"), count=99, overflowCount=10
            ),
            antd.Badge(
                html.a(href="#", className="head-example"),
                count=1000,
                overflowCount=999,
            ),
        ],
        direction="vertical",
    )
