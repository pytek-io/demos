import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    shape = antd.Radio.Group(
        [antd.Radio("Circle", value="circle"), antd.Radio("Square", value="square")]
    )
    return html.div(
        [
            shape,
            antd.FloatButton(
                icon=ant_icons.CustomerServiceOutlined(), shape=shape, type="primary"
            ),
        ]
    )
