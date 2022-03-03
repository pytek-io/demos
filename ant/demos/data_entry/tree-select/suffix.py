from reflect_html import *
from reflect_antd import TreeSelect
from reflect_ant_icons import SmileOutlined

from reflect import autorun

TreeNode = TreeSelect.TreeNode


def app():
    icon = SmileOutlined()
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
        suffixIcon=icon,
        style=dict(width="100%"),
        dropdownStyle=dict(maxHeight=400, overflow="auto"),
        placeholder="Please select",
        allowClear=True,
        treeDefaultExpandAll=True,
    )
    autorun(lambda: print("selected", tree_select()))
    return tree_select
