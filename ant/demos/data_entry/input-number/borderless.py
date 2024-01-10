import render_antd as antd
import render_html as html


def app(_):
    return antd.InputNumber(min=1, max=10, defaultValue=3, bordered=False)
