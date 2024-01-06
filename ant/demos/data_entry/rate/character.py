import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Rate(character=ant_icons.HeartOutlined([]), allowHalf=True),
            html.br(),
            antd.Rate(character="A", allowHalf=True, style={"fontSize": 36}),
            html.br(),
            antd.Rate(character="好", allowHalf=True),
        ]
    )
