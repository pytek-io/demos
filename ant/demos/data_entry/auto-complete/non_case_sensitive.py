from reflect_html import *
from reflect_antd import AutoComplete
from reflect import js

options = [
    {"value": "Burns Bay Road"},
    {"value": "Downing Street"},
    {"value": "Wall Street"},
]


def app():
    return AutoComplete(
        style=dict(width=200),
        options=options,
        placeholder="try to type `b`",
        filterOption=js("autoCompleteFilterOption"),
    )
