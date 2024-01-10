import render_antd as antd
import render_html as html


def dig(path="0", level=3):
    result = []
    for i in range(10):
        key = f"{path}-{i}"
        treeNode = {"title": key, "key": key}
        if level > 0:
            treeNode["children"] = dig(key, level - 1)
            result.append(treeNode)
    return result


def app(_):
    treeData = dig()
    return antd.Tree(treeData=treeData, height=233, defaultExpandAll=True)
