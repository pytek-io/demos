import reflect as r
import reflect_antd as antd
import reflect_html as html

TreeNode = antd.TreeSelect.TreeNode


def app():
    tree_select = antd.TreeSelect(
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
                    [
                        TreeNode(
                            value="sss", title=html.b("sss", style={"color": "#08c"})
                        )
                    ],
                    value="parent 1-1",
                    title="parent 1-1",
                ),
            ],
            value="parent 1",
            title="parent 1",
        ),
        showSearch=True,
        style={"width": "100%"},
        dropdownStyle={"maxHeight": 400, "overflow": "auto"},
        placeholder="Please select",
        allowClear=True,
        multiple=True,
        treeDefaultExpandAll=True,
    )
    r.autorun(lambda: print("selected", tree_select()))
    return tree_select
