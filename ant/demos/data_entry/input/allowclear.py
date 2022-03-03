from reflect_html import *
from reflect_antd import Input

from reflect import autorun

TextArea = Input.TextArea


def app():
    input_ = Input(placeholder="input with clear icon", allowClear=True)
    text_area = TextArea(placeholder="textarea with clear icon", allowClear=True)
    autorun(lambda: print(input_()))
    autorun(lambda: print(text_area()))
    return [input_, br(), br(), text_area]
