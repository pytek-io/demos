import render_antd as antd
import render_html as html


def app():
    return antd.FloatButton(tooltip=html.div("Documents"))
