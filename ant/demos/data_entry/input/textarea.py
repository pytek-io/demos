import reflect_antd as antd
import reflect_html as html

TextArea = antd.Input.TextArea


def app():
    return TextArea(rows=4)
