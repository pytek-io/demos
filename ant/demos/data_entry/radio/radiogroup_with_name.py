import render_antd as antd
import render_html as html


def app(_):
    return antd.Radio.Group(
        [
            antd.Radio("A", value=1),
            antd.Radio("B", value=2),
            antd.Radio("C", value=3),
            antd.Radio("D", value=4),
        ],
        name="radiogroup",
        defaultValue=1,
    )
