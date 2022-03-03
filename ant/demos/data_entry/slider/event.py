from reflect_html import *
from reflect_antd import Slider
from reflect import Callback
from reflect import autorun


def onAfterChange(value):
    print("onAfterChange", value)


def app():
    slider1 = Slider(
        defaultValue=30, onAfterChange=Callback(onAfterChange)
    )
    autorun(lambda: print("onChange", slider1()))
    slider2 = Slider(
        range=True,
        step=10,
        defaultValue=[20, 50],
        onAfterChange=Callback(onAfterChange),
    )
    autorun(lambda: print("onChange", slider2()))
    return [
        slider1,
        slider2,
    ]
