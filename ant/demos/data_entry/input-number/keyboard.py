import reflect_antd as antd
import reflect_html as html


def app():
    switch = antd.Switch("Toggle keyboard")
    return html.div(
        [antd.InputNumber(min=1, max=10, keyboard=switch, defaultValue=3), switch]
    )
