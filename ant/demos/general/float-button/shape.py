import reflect_antd as antd
import reflect_html as html
import reflect_ant_icons as ant_icons


def app():
    return html.div(
        [
            antd.FloatButton(
                shape="square",
                icon=ant_icons.CustomerServiceOutlined(),
                type="primary",
                style={"right": 94},
            ),
            antd.FloatButton(
                shape="circle",
                icon=ant_icons.CustomerServiceOutlined(),
                type="primary",
                style={"right": 24},
            ),
        ]
    )
