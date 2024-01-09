import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


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
