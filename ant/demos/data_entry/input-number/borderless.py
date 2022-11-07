import reflect_antd as antd
import reflect_html as html


def app():
    return antd.InputNumber(min=1, max=10, defaultValue=3, bordered=False)
