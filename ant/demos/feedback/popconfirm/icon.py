import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app(_):
    return antd.Popconfirm(
        html.a("Delete", href="#"),
        title="Are you sure？",
        icon=ant_icons.QuestionCircleOutlined(style={"color": "red"}),
    )
