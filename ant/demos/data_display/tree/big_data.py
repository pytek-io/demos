from reflect_html import *
from reflect_antd import Tree


def app():

    treeData = []

    for i in range(100):
        children = []

        for j in range(100):
            children.append(
                {
                    "title": f"child {i}-{j}",
                    "key": f"l-{i}-{j}",
                }
            )

        treeData.append(
            {
                "title": f"parent {i}",
                "key": f"l-{i}",
                "children": children,
            }
        )

    return Tree(defaultExpandAll=True, height=400, treeData=treeData)