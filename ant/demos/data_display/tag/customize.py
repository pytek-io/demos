import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Tag("Tag1", closeIcon="关 闭"),
            antd.Tag("Tag2", closeIcon=ant_icons.CloseCircleOutlined([])),
        ]
    )
