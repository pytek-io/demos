import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            html.div("Scroll to bottom"),
            html.div("Scroll to bottom"),
            html.div("Scroll to bottom"),
            html.div("Scroll to bottom"),
            html.div("Scroll to bottom"),
            html.div("Scroll to bottom"),
            html.div("Scroll to bottom"),
            antd.FloatButton.BackTop(),
        ],
        style={"height": "300vh", "padding": 10},
    )
