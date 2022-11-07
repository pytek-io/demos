import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    input1 = antd.InputNumber(size="large", min=1, max=100000, defaultValue=3)
    input2 = antd.InputNumber(min=1, max=100000, defaultValue=3)
    input3 = antd.InputNumber(size="small", min=1, max=100000, defaultValue=3)
    r.autorun(lambda: print("changed", input1()))
    r.autorun(lambda: print("changed", input2()))
    r.autorun(lambda: print("changed", input3()))
    return html.div([input1, input2, input3], className="site-input-number-wrapper")
