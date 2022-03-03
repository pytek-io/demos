from reflect_html import *
from reflect_antd import Input

TextArea = Input.TextArea


def app():
    return TextArea(showCount=True, maxLength=100)
