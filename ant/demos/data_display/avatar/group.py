import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Avatar.Group(
                [
                    antd.Avatar(
                        src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                    ),
                    antd.Avatar("K", style={"backgroundColor": "#f56a00"}),
                    antd.Tooltip(
                        antd.Avatar(
                            style={"backgroundColor": "#87d068"},
                            icon=ant_icons.UserOutlined([]),
                        ),
                        title="Ant User",
                        placement="top",
                    ),
                    antd.Avatar(
                        style={"backgroundColor": "#1890ff"},
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
                    antd.Avatar("K", style={"backgroundColor": "#f56a00"}),
                    antd.Tooltip(
                        antd.Avatar(
                            style={"backgroundColor": "#87d068"},
                            icon=ant_icons.UserOutlined([]),
                        ),
                        title="Ant User",
                        placement="top",
                    ),
                    antd.Avatar(
                        style={"backgroundColor": "#1890ff"},
                        icon=ant_icons.AntDesignOutlined([]),
                    ),
                ],
                maxCount=2,
                maxStyle={"color": "#f56a00", "backgroundColor": "#fde3cf"},
            ),
            antd.Divider(),
            antd.Avatar.Group(
                [
                    antd.Avatar(
                        src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                    ),
                    antd.Avatar("K", style={"backgroundColor": "#f56a00"}),
                    antd.Tooltip(
                        antd.Avatar(
                            style={"backgroundColor": "#87d068"},
                            icon=ant_icons.UserOutlined([]),
                        ),
                        title="Ant User",
                        placement="top",
                    ),
                    antd.Avatar(
                        style={"backgroundColor": "#1890ff"},
                        icon=ant_icons.AntDesignOutlined([]),
                    ),
                ],
                maxCount=2,
                size="large",
                maxStyle={"color": "#f56a00", "backgroundColor": "#fde3cf"},
            ),
        ]
    )
