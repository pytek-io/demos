import render as r
import render_antd as antd
import render_html as html

SHOW_PARENT = antd.TreeSelect.SHOW_PARENT
treeData = [
    {
        "title": "Node1",
        "value": "0-0",
        "key": "0-0",
        "children": [{"title": "Child Node1", "value": "0-0-0", "key": "0-0-0"}],
    },
    {
        "title": "Node2",
        "value": "0-1",
        "key": "0-1",
        "children": [
            {"title": "Child Node3", "value": "0-1-0", "key": "0-1-0"},
            {"title": "Child Node4", "value": "0-1-1", "key": "0-1-1"},
            {"title": "Child Node5", "value": "0-1-2", "key": "0-1-2"},
        ],
    },
]


def app(_):
    tree_select = antd.TreeSelect(
        treeCheckable=True,
        treeData=treeData,
        showCheckedStrategy=SHOW_PARENT,
        placeholder="Please select",
        style={"width": "100%"},
    )
    r.autorun(lambda: print("selected", tree_select()))
    return tree_select
