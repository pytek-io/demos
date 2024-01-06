from functools import partial

import render_antd as antd
import render_html as html


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
                            "title": html.span("sss", style={"color": "#1890ff"}),
                            "key": "0-0-1-0",
                        }
                    ],
                },
            ],
        }
    ]
    return antd.Tree(
        checkable=True,
        defaultExpandedKeys=["0-0-0", "0-0-1"],
        defaultSelectedKeys=["0-0-0", "0-0-1"],
        defaultCheckedKeys=["0-0-0", "0-0-1"],
        onSelect=partial(print, "selected"),
        onCheck=partial(print, "checked"),
        treeData=treeData,
    )
