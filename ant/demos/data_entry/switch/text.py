import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Switch(
                checkedChildren="开启", unCheckedChildren="关闭", defaultChecked=True
            ),
            html.br(),
            antd.Switch(checkedChildren="1", unCheckedChildren="0"),
            html.br(),
            antd.Switch(
                checkedChildren=ant_icons.CheckOutlined([]),
                unCheckedChildren=ant_icons.CloseOutlined([]),
                defaultChecked=True,
            ),
        ]
    )
