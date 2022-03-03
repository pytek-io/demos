from reflect_html import *
from reflect_antd import Slider
from reflect import JSMethod


percent_formatter = JSMethod("percent_formatter", "return `${value}%`", "value")


def app():
    return [
        Slider(tipFormatter=percent_formatter, defaultValue=0),
        Slider(),
    ]
