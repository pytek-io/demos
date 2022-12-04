import reflect_antd as antd
import reflect_html as html


def app():
    treeData = []
    for i in range(100):
        children = []
        for j in range(100):
            children.append({"title": f"child {i}-{j}", "key": f"l-{i}-{j}"})
        treeData.append({"title": f"parent {i}", "key": f"l-{i}", "children": children})
    return antd.Tree(defaultExpandAll=True, height=400, treeData=treeData)
