from reflect_html import *
from reflect_antd import InputNumber


def app():
    return InputNumber(min=1, max=10, defaultValue=3, bordered=False)
