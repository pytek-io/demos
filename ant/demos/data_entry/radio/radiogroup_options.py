from reflect_html import *
from reflect_antd import Radio
from reflect import Callback
from reflect import autorun


plain_options = ["Apple", "Pear", "Orange"]
options = [
    {"label": "Apple", "value": "Apple"},
    {"label": "Pear", "value": "Pear"},
    {"label": "Orange", "value": "Orange"},
]
options_with_disabled = [
    {"label": "Apple", "value": "Apple"},
    {"label": "Pear", "value": "Pear"},
    {"label": "Orange", "value": "Orange", "disabled": True},
]


def app():
    radio_group1 = Radio.Group(
        options=plain_options,
        defaultValue="Apple",
    )
    radio_group2 = Radio.Group(
        options=options_with_disabled,
        defaultValue="Apple",
    )
    radio_group3 = Radio.Group(
        options=options,
        defaultValue="Apple",
        optionType="button",
    )
    radio_group4 = Radio.Group(
        options=options_with_disabled,
        defaultValue="Apple",
        optionType="button",
        buttonStyle="solid",
    )
    autorun(lambda: print("radio1 checked", radio_group1()))
    autorun(lambda: print("radio2 checked", radio_group2()))
    autorun(lambda: print("radio3 checked", radio_group3()))
    autorun(lambda: print("radio4 checked", radio_group4()))
    return div(
        [
            radio_group1,
            br(),
            radio_group2,
            br(),
            br(),
            radio_group3,
            br(),
            br(),
            radio_group4,
        ]
    )
