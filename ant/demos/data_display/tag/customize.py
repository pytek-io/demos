import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Tag("Tag1", closable=True, closeIcon="关 闭"),
            antd.Tag(
                "Tag2", closable=True, closeIcon=ant_icons.CloseCircleOutlined([])
            ),
        ]
    )
