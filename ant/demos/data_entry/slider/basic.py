from reflect_html import *
from reflect_antd import Slider, Switch

from reflect import autorun


def app():
    disable_switch = Switch(size="small")
    slider1 = Slider(defaultValue=30, disabled=disable_switch)
    slider2 = Slider(range=True, defaultValue=[20, 50], disabled=disable_switch)
    autorun(lambda: print(slider1()))
    autorun(lambda: print(slider2()))
    return [
        slider1,
        slider2,
        "Disabled: ",
        disable_switch,
    ]
