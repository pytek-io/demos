import render_antd as antd
import render_html as html

TextArea = antd.Input.TextArea


def app():
    return TextArea(showCount=True, maxLength=100)
