import render_antd as antd

TextArea = antd.Input.TextArea


def app(_):
    return TextArea(rows=4)
