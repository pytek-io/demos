from reflect_html import *
from reflect_antd import Tree


def dig(path="0", level=3):
    result = []
    for i in range(10):
        key = f"{path}-{i}"
        treeNode = dict(title=key, key=key)
        if level > 0:
            treeNode["children"] = dig(key, level - 1)
            result.append(treeNode)
    return result


def app():
    treeData = dig()
    return Tree(treeData=treeData, height=233, defaultExpandAll=True)
