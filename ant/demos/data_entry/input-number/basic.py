import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    input_number = antd.InputNumber(min=1, max=10, defaultValue=3)
    r.autorun(lambda: print(input_number()))
    return input_number
