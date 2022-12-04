import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Tag("Tag1", closable=True, closeIcon="关 闭"),
            antd.Tag(
                "Tag2", closable=True, closeIcon=ant_icons.CloseCircleOutlined([])
            ),
        ]
    )
