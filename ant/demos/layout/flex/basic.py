import render_antd as antd
import render_html as html

baseStyle = {"width": "25%", "height": 54}


def app():
    orientation = antd.Radio.Group(
        [
            antd.Radio("horizontal", value=False),
            antd.Radio("vertical", value=True),
        ],
    )
    return antd.Flex(
        [
            orientation,
            antd.Flex(
                [html.div(i, style=baseStyle) for i in range(4)],
                vertical=orientation,
            ),
        ],
        gap="middle",
        vertical=True,
    )
