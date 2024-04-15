import render as r
import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


tree_data = [
    {
        "value": "parent 1",
        "title": "parent 1",
        "children": [
            {
                "value": "parent 1-0",
                "title": "parent 1-0",
                "children": [
                    {"value": "leaf1", "title": "my leaf"},
                    {"value": "leaf2", "title": "your leaf"},
                ],
            },
            {
                "value": "parent 1-1",
                "title": html.b("sss", style={"color": "#08c"}),
                "children": [{"value": "sss", "title": "sss"}],
            },
        ],
    }
]


def app(_):
    icon = ant_icons.SmileOutlined()
    tree_select = antd.TreeSelect(
        treeData=tree_data,
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
