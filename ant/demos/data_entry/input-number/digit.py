import render as r
import render_antd as antd
import render_html as html


def app(_):
    result = antd.InputNumber(min=0, max=10, step=0.1)
    r.autorun(lambda: print("changed", result()))
    return result
