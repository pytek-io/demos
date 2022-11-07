import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Popconfirm(
        html.a("Delete", href="#"),
        title="Are you sure？",
        icon=ant_icons.QuestionCircleOutlined(style={"color": "red"}),
    )
