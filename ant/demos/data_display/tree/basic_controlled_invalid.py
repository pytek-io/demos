from render_antd import Tree
from render_html import *

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


def app(_):
    return Demo()
