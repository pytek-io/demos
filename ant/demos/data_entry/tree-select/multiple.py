from reflect_html import *
from reflect_antd import TreeSelect

from reflect import autorun

TreeNode = TreeSelect.TreeNode


def app():
    tree_select = TreeSelect(
        TreeNode(
            [
                TreeNode(
                    [
                        TreeNode(value="leaf1", title="my leaf"),
                        TreeNode(value="leaf2", title="your leaf"),
                    ],
                    value="parent 1-0",
                    title="parent 1-0",
                ),
                TreeNode(
                    [TreeNode(value="sss", title=b("sss", style={"color": "#08c"}))],
                    value="parent 1-1",
                    title="parent 1-1",
                ),
            ],
            value="parent 1",
            title="parent 1",
        ),
        showSearch=True,
        style=dict(width="100%"),
        dropdownStyle=dict(maxHeight=400, overflow="auto"),
        placeholder="Please select",
        allowClear=True,
        multiple=True,
        treeDefaultExpandAll=True,
    )
    autorun(lambda: print("selected", tree_select()))
    return tree_select
