from reflect_html import *
from reflect_antd import Tree
from reflect import Callback


def app():
    x = 3
    y = 2
    z = 1
    gData = []

    def generateData(_level, _preKey=None, _tns=None):
        nonlocal gData
        preKey = _preKey or 0
        tns = gData if _tns is None else _tns

        children = []
        for i in range(x):
            key = f"{preKey}-{i}"
            tns.append({"title": key, "key": key})
            if i < y:
                children.append(key)
        if _level < 0:
            return tns
        level = _level - 1
        for index, key in enumerate(children):
            tns[index]["children"] = []
            generateData(level, key, tns[index]["children"])

    generateData(z)
    return Tree(
        className="draggable-tree",
        defaultExpandedKeys=["0-0", "0-0-0", "0-0-0-0"],
        draggable=True,
        blockNode=True,
        onDragEnter=Callback(lambda x: print("enter", x), args="node.key"),
        onDrop=Callback(lambda x: print("drop", x), args="node.key"),
        treeData=gData,
    )
