from reflect_html import *
from reflect_antd import Tree

onSelect = Tree(
    checkable=True,
    onExpand=onExpand,
    expandedKeys=expandedKeys,
    autoExpandParent=autoExpandParent,
    onCheck=onCheck,
    checkedKeys=checkedKeys,
    onSelect=onSelect,
    selectedKeys=selectedKeys,
    treeData=treeData,
)


def app():
    return Demo()
