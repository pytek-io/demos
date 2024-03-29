import render as r
import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html

TreeNode = antd.TreeSelect.TreeNode


def app(_):
    icon = ant_icons.SmileOutlined()
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
        suffixIcon=icon,
        style={"width": "100%"},
        dropdownStyle={"maxHeight": 400, "overflow": "auto"},
        placeholder="Please select",
        allowClear=True,
        treeDefaultExpandAll=True,
    )
    r.autorun(lambda: print("selected", tree_select()))
    return tree_select
