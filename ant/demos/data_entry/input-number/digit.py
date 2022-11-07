import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    result = antd.InputNumber(min=0, max=10, step=0.1)
    r.autorun(lambda: print("changed", result()))
    return result
