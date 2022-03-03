from reflect_html import *
from reflect_antd import InputNumber

from reflect import autorun


def app():
    result = InputNumber(min=0, max=10, step=0.1)
    autorun(lambda: print("changed", result()))
    return result
