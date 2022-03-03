from reflect_html import *
from reflect_antd import Avatar, Divider, Tooltip
from reflect_ant_icons import UserOutlined, AntDesignOutlined


def app():
    return [
        Avatar.Group(
            [
                Avatar(
                    src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                ),
                Avatar("K", style=dict(backgroundColor="#f56a00")),
                Tooltip(
                    Avatar(
                        style=dict(backgroundColor="#87d068"), icon=UserOutlined([])
                    ),
                    title="Ant User",
                    placement="top",
                ),
                Avatar(
                    style=dict(backgroundColor="#1890ff"), icon=AntDesignOutlined([])
                ),
            ]
        ),
        Divider(),
        Avatar.Group(
            [
                Avatar(
                    src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                ),
                Avatar("K", style=dict(backgroundColor="#f56a00")),
                Tooltip(
                    Avatar(
                        style=dict(backgroundColor="#87d068"), icon=UserOutlined([])
                    ),
                    title="Ant User",
                    placement="top",
                ),
                Avatar(
                    style=dict(backgroundColor="#1890ff"), icon=AntDesignOutlined([])
                ),
            ],
            maxCount=2,
            maxStyle=dict(color="#f56a00", backgroundColor="#fde3cf"),
        ),
        Divider(),
        Avatar.Group(
            [
                Avatar(
                    src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
                ),
                Avatar("K", style=dict(backgroundColor="#f56a00")),
                Tooltip(
                    Avatar(
                        style=dict(backgroundColor="#87d068"), icon=UserOutlined([])
                    ),
                    title="Ant User",
                    placement="top",
                ),
                Avatar(
                    style=dict(backgroundColor="#1890ff"), icon=AntDesignOutlined([])
                ),
            ],
            maxCount=2,
            size="large",
            maxStyle=dict(color="#f56a00", backgroundColor="#fde3cf"),
        ),
    ]
