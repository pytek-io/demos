import render as r
import render_antd as antd

options = [
    {"value": "Burns Bay Road"},
    {"value": "Downing Street"},
    {"value": "Wall Street"},
]

filterOption = r.js_arrow(
    "list_item_renderer",
    "(inputValue, {value}) => value.toUpperCase().indexOf(inputValue.toUpperCase()) !== -1;",
)


def app(_):
    return antd.AutoComplete(
        style={"width": 200},
        options=options,
        placeholder="try to type 'b'",
        filterOption=filterOption,
    )
