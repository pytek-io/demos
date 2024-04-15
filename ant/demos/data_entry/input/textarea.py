import render_antd as antd

TextArea = antd.Input.TextArea


def app(_):
    return TextArea(autoSize={"minRows": 4, "maxRows": 6}, defaultValue="Hello\nWorld")
