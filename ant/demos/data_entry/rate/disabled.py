import render_antd as antd
import render_html as html


def app(_):
    return antd.Rate(disabled=True, defaultValue=2)
