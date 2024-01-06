from render_html import *
from render_antd import Tree

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
