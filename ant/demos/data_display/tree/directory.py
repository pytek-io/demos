from functools import partial

import render_antd as antd


def app(_):
    treeData = [
        {
            "title": "parent 0",
            "key": "0-0",
            "children": [
                {"title": "leaf 0-0", "key": "0-0-0", "isLeaf": True},
                {"title": "leaf 0-1", "key": "0-0-1", "isLeaf": True},
            ],
        },
        {
            "title": "parent 1",
            "key": "0-1",
            "children": [
                {"title": "leaf 1-0", "key": "0-1-0", "isLeaf": True},
                {"title": "leaf 1-1", "key": "0-1-1", "isLeaf": True},
            ],
        },
    ]
    return antd.Tree.DirectoryTree(
        multiple=True,
        defaultExpandAll=True,
        onSelect=partial(print, "selected"),
        onExpand=partial(print, "expanded"),
        treeData=treeData,
    )
