from reflect_html import *
from reflect_antd import TreeSelect

from reflect import autorun

treeData = [
    {
        "title": "Node1",
        "value": "0-0",
        "children": [
            {
                "title": "Child Node1",
                "value": "0-0-1",
            },
            {
                "title": "Child Node2",
                "value": "0-0-2",
            },
        ],
    },
    {
        "title": "Node2",
        "value": "0-1",
    },
]


def app():
    tree_select = TreeSelect(
        style=dict(width="100%"),
        dropdownStyle=dict(maxHeight=400, overflow="auto"),
        treeData=treeData,
        placeholder="Please select",
        treeDefaultExpandAll=True,
    )
    autorun(lambda: print("selected", tree_select()))
    return tree_select