import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Rate(allowHalf=True, defaultValue=2.5)
