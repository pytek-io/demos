from reflect_html import *
from reflect_antd import InputNumber

from reflect import autorun


def app():
    input1 = InputNumber(
        size="large",
        min=1,
        max=100000,
        defaultValue=3,
    )
    input2 = InputNumber(min=1, max=100000, defaultValue=3)
    input3 = InputNumber(size="small", min=1, max=100000, defaultValue=3)
    autorun(lambda: print("changed", input1()))
    autorun(lambda: print("changed", input2()))
    autorun(lambda: print("changed", input3()))
    return div(
        [input1, input2, input3],
        className="site-input-number-wrapper",
    )
