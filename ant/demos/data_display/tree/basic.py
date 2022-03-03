from reflect_html import *
from reflect_antd import Tree
from reflect import Callback


def app():
    treeData = [
        {
            "title": "parent 1",
            "key": "0-0",
            "children": [
                {
                    "title": "parent 1-0",
                    "key": "0-0-0",
                    "disabled": True,
                    "children": [
                        {"title": "leaf", "key": "0-0-0-0", "disableCheckbox": True},
                        {"title": "leaf", "key": "0-0-0-1"},
                    ],
                },
                {
                    "title": "parent 1-1",
                    "key": "0-0-1",
                    "children": [
                        {
                            "title": span("sss", style={"color": "#1890ff"}),
                            "key": "0-0-1-0",
                        }
                    ],
                },
            ],
        }
    ]

    return Tree(
        checkable=True,
        defaultExpandedKeys=["0-0-0", "0-0-1"],
        defaultSelectedKeys=["0-0-0", "0-0-1"],
        defaultCheckedKeys=["0-0-0", "0-0-1"],
        onSelect=Callback(
            lambda keys: print("selected", keys)
        ),
        onCheck=Callback(
            lambda keys: print("checked", keys)
        ),
        treeData=treeData,
    )
