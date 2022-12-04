import reflect as r
import reflect_antd as antd

DirectoryTree = antd.Tree.DirectoryTree


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
        onSelect=r.Callback(lambda keys: print("selected", keys)),
        onExpand=r.Callback(lambda keys: print("expanded", keys)),
        treeData=treeData,
    )
