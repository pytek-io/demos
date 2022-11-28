import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Avatar.Group(
                [
                    antd.Avatar(
                        src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                    ),
                    antd.Avatar("K", style=dict(backgroundColor="#f56a00")),
                    antd.Tooltip(
                        antd.Avatar(
                            style=dict(backgroundColor="#87d068"),
                            icon=ant_icons.UserOutlined([]),
                        ),
                        title="Ant User",
                        placement="top",
                    ),
                    antd.Avatar(
                        style=dict(backgroundColor="#1890ff"),
                        icon=ant_icons.AntDesignOutlined([]),
                    ),
                ]
            ),
            antd.Divider(),
            antd.Avatar.Group(
                [
                    antd.Avatar(
                        src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                    ),
                    antd.Avatar("K", style=dict(backgroundColor="#f56a00")),
                    antd.Tooltip(
                        antd.Avatar(
                            style=dict(backgroundColor="#87d068"),
                            icon=ant_icons.UserOutlined([]),
                        ),
                        title="Ant User",
                        placement="top",
                    ),
                    antd.Avatar(
                        style=dict(backgroundColor="#1890ff"),
                        icon=ant_icons.AntDesignOutlined([]),
                    ),
                ],
                maxCount=2,
                maxStyle=dict(color="#f56a00", backgroundColor="#fde3cf"),
            ),
            antd.Divider(),
            antd.Avatar.Group(
                [
                    antd.Avatar(
                        src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                    ),
                    antd.Avatar("K", style=dict(backgroundColor="#f56a00")),
                    antd.Tooltip(
                        antd.Avatar(
                            style=dict(backgroundColor="#87d068"),
                            icon=ant_icons.UserOutlined([]),
                        ),
                        title="Ant User",
                        placement="top",
                    ),
                    antd.Avatar(
                        style=dict(backgroundColor="#1890ff"),
                        icon=ant_icons.AntDesignOutlined([]),
                    ),
                ],
                maxCount=2,
                size="large",
                maxStyle=dict(color="#f56a00", backgroundColor="#fde3cf"),
            ),
        ]
    )
