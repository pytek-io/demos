import reflect as r
import reflect_antd as antd

options = [
    {"value": "Burns Bay Road"},
    {"value": "Downing Street"},
    {"value": "Wall Street"},
]

filterOption = r.JSMethod(
    "list_item_renderer",
    "return option.value.toUpperCase().indexOf(inputValue.toUpperCase()) !== -1;",
    "inputValue",
    "option",
)


def app():
    return antd.AutoComplete(
        style={"width": 200},
        options=options,
        placeholder="try to type `b`",
        filterOption=filterOption,
    )
