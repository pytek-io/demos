from reflect_html import *
from reflect_antd import Checkbox

from reflect import make_observable, autorun

PLAIN_OPTIONS = ["Apple", "Pear", "Orange"]
OPTIONS = [
    {"label": "Apple", "value": "Apple"},
    {"label": "Pear", "value": "Pear"},
    {"label": "Orange", "value": "Orange"},
]
OPTIONS_WITH_DISABLED = [
    {"label": "Apple", "value": "Apple"},
    {"label": "Pear", "value": "Pear"},
    {"label": "Orange", "value": "Orange", "disabled": False},
]


def app():
    check_box1 = Checkbox.Group(options=PLAIN_OPTIONS, defaultValue=["Apple"])
    check_box2 = Checkbox.Group(options=OPTIONS, defaultValue=["Pear"])
    check_box3 = Checkbox.Group(
        options=OPTIONS_WITH_DISABLED, disabled=True, defaultValue=["Apple"]
    )
    autorun(lambda: print("checked values", check_box1()))
    autorun(lambda: print("checked values", check_box2()))
    autorun(lambda: print("checked values", check_box3()))

    return [
        check_box1,
        br(),
        br(),
        check_box2,
        br(),
        br(),
        check_box3,
    ]
