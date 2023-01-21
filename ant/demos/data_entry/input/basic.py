import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    text_input = antd.Input(placeholder="Basic usage")
    r.autorun(lambda: print(text_input()))
    return text_input
