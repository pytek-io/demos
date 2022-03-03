from reflect_html import *
from reflect_antd import Slider, Switch


def app():
    reverse_switch = Switch(size="small")
    return [
        Slider(defaultValue=30, reverse=reverse_switch),
        Slider(range=True, defaultValue=[20, 50], reverse=reverse_switch),
        "Reversed: ",
        reverse_switch,
    ]
