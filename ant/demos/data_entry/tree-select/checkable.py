from reflect_html import *
from reflect_antd import TreeSelect

from reflect import autorun

SHOW_PARENT = TreeSelect.SHOW_PARENT

treeData = [
    {
        "title": "Node1",
        "value": "0-0",
        "key": "0-0",
        "children": [
            {
                "title": "Child Node1",
                "value": "0-0-0",
                "key": "0-0-0",
            },
        ],
    },
    {
        "title": "Node2",
        "value": "0-1",
        "key": "0-1",
        "children": [
            {
                "title": "Child Node3",
                "value": "0-1-0",
                "key": "0-1-0",
            },
            {
                "title": "Child Node4",
                "value": "0-1-1",
                "key": "0-1-1",
            },
            {
                "title": "Child Node5",
                "value": "0-1-2",
                "key": "0-1-2",
            },
        ],
    },
]


def app():
    tree_select = TreeSelect(
        treeCheckable= True,
        treeData=treeData,
        showCheckedStrategy= SHOW_PARENT,
        placeholder="Please select",
        style=dict(width="100%"),
    )
    autorun(lambda: print("selected", tree_select()))
    return tree_select