import render_antd as antd
import render_html as html


def app():
    return antd.Rate(allowHalf=True, defaultValue=2.5)
