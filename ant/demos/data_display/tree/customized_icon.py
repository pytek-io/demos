from reflect_html import *
from reflect_antd import Tree
from reflect_ant_icons import (
    DownOutlined,
    FrownOutlined,
    SmileOutlined,
    MehOutlined,
    FrownFilled,
)
from reflect import js


def app():
    treeData = [
        {
            "title": "parent 1",
            "key": "0-0",
            "icon": SmileOutlined(),
            "children": [
                {
                    "title": "leaf",
                    "key": "0-0-0",
                    "icon": MehOutlined(),
                },
                {
                    "title": "leaf",
                    "key": "0-0-1",
                    "icon": js("custom_icon"),
                },
            ],
        },
    ]

    return Tree(
        showIcon=True,
        defaultExpandAll=True,
        defaultSelectedKeys=["0-0-0"],
        switcherIcon=DownOutlined([]),
        treeData=treeData,
    )
