import render as r
import render_antd as antd
import render_html as html


def app(_):
    text_input = antd.Input(placeholder="Basic usage")
    r.autorun(lambda: print(text_input()))
    return text_input
