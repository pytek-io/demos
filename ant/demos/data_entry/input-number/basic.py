from reflect_html import *
from reflect_antd import InputNumber

from reflect import autorun


def app():
    input_number = InputNumber(min=1, max=10, defaultValue=3)
    autorun(lambda: print(input_number()))
    return input_number