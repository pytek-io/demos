import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Rate(character=ant_icons.HeartOutlined([]), allowHalf=True),
            html.br(),
            antd.Rate(character="A", allowHalf=True, style=dict(fontSize=36)),
            html.br(),
            antd.Rate(character="好", allowHalf=True),
        ]
    )
