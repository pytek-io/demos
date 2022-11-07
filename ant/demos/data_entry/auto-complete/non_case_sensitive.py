import reflect as r
import reflect_antd as antd
import reflect_html as html

options = [
    {"value": "Burns Bay Road"},
    {"value": "Downing Street"},
    {"value": "Wall Street"},
]


def app():
    return antd.AutoComplete(
        style=dict(width=200),
        options=options,
        placeholder="try to type `b`",
        filterOption=r.js("autoCompleteFilterOption"),
    )
