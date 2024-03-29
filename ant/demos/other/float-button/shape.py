import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app(_):
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
