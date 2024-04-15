import render as r
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
    tree_select = antd.TreeSelect(
        treeData=tree_data,
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
