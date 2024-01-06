import render_antd as antd

TextArea = antd.Input.TextArea


def app():
    return TextArea(rows=4)
