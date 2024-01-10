import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Input(
                size="large",
                placeholder="large size",
                prefix=ant_icons.UserOutlined([]),
            ),
            html.br(),
            html.br(),
            antd.Input(placeholder="default size", prefix=ant_icons.UserOutlined([])),
            html.br(),
            html.br(),
            antd.Input(
                size="small",
                placeholder="small size",
                prefix=ant_icons.UserOutlined([]),
            ),
        ]
    )
