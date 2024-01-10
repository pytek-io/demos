import render_antd as antd
import render_html as html


def app(_):
    return antd.Rate(allowHalf=True, defaultValue=2.5)
