import asyncio

import reflect as r
import reflect_antd as antd


def app():
    node_id = 0
    nodes = {}

    def generate_nodes():
        nonlocal node_id, nodes
        for i in range(3):
            is_leaf = i < 1
            title = "Tree Node" if is_leaf else "Expand to load"
            data = {
                "id": f"{node_id}",
                "pId": f"{i}",
                "value": f"{i}",
                "key": f"{node_id}",
                "title": title,
                "isLeaf": is_leaf,
            }
            nodes[f"{node_id}"] = data
            node_id += 1
            yield data

    treeData = r.create_observable(list(generate_nodes()))

    async def load_data(current_node_id):
        await asyncio.sleep(0.5)
        nodes[current_node_id]["children"] = list(generate_nodes())
        treeData.touch()

    return antd.Tree(
        style=dict(width="100%"),
        loadData=r.Callback(load_data, args="id", is_promise=True),
        treeData=treeData,
        onSelect=r.Callback(lambda x: print(x)),
    )
