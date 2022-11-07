import reflect as r
import reflect_antd as antd
import reflect_html as html

treeData = [
    {
        "title": "Node1",
        "value": "0-0",
        "children": [
            {"title": "Child Node1", "value": "0-0-1"},
            {"title": "Child Node2", "value": "0-0-2"},
        ],
    },
    {"title": "Node2", "value": "0-1"},
]


def app():
    tree_select = antd.TreeSelect(
        style=dict(width="100%"),
        dropdownStyle=dict(maxHeight=400, overflow="auto"),
        treeData=treeData,
        placeholder="Please select",
        treeDefaultExpandAll=True,
    )
    r.autorun(lambda: print("selected", tree_select()))
    return tree_select
