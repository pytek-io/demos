from reflect_html import *
from reflect_antd import Tree
from reflect import Callback

DirectoryTree = Tree.DirectoryTree


def app():
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

    return DirectoryTree(
        multiple=True,
        defaultExpandAll=True,
        onSelect=Callback(
            lambda keys: print("selected", keys)
        ),
        onExpand=Callback(
            lambda keys: print("expanded", keys)
        ),
        treeData=treeData,
    )
