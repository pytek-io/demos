import reflect as r
import reflect_ant_icons as ant_icons
import reflect_antd as antd

custom_icon = r.JSMethod(
    "custom_icon",
    """return createElement(reflect_ant_icons[selected ? "FrownFilled" : "FrownOutlined"]);""",
    "selected",
)


def app():
    treeData = [
        {
            "title": "parent 1",
            "key": "0-0",
            "icon": ant_icons.SmileOutlined(),
            "children": [
                {"title": "leaf", "key": "0-0-0", "icon": ant_icons.MehOutlined()},
                {"title": "leaf", "key": "0-0-1", "icon": custom_icon},
            ],
        }
    ]
    return antd.Tree(
        showIcon=True,
        defaultExpandAll=True,
        defaultSelectedKeys=["0-0-0"],
        switcherIcon=ant_icons.DownOutlined([]),
        treeData=treeData,
    )
