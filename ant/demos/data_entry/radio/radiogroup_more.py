from reflect_html import *
from reflect_antd import Radio, Input
from reflect import create_observable


radioStyle = {
    "display": "block",
    "height": "30px",
    "lineHeight": "30px",
}


def onChange(value):
    print("radio checked", value)


def app():
    value = create_observable(1)
    return Radio.Group(
        [
            Radio("Option A", style=radioStyle, value=1),
            Radio("Option B", style=radioStyle, value=2),
            Radio("Option C", style=radioStyle, value=3),
            Radio(
                Input(style={"width": 100, "height": 30}) if value() == 4 else None,
                style=radioStyle,
                value=4,
            ),
        ],
        onChange=onChange,
        value=value,
    )
