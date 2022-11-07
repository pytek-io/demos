import reflect as r
import reflect_antd as antd
import reflect_html as html

radioStyle = {"display": "block", "height": "30px", "lineHeight": "30px"}


def onChange(value):
    print("radio checked", value)


def app():
    value = r.create_observable(1)
    return antd.Radio.Group(
        [
            antd.Radio("Option A", style=radioStyle, value=1),
            antd.Radio("Option B", style=radioStyle, value=2),
            antd.Radio("Option C", style=radioStyle, value=3),
            antd.Radio(
                antd.Input(style={"width": 100, "height": 30})
                if value() == 4
                else None,
                style=radioStyle,
                value=4,
            ),
        ],
        onChange=onChange,
        value=value,
    )
