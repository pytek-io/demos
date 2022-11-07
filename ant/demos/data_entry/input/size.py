import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
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
