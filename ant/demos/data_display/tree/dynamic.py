import asyncio
from typing import Dict, List

import render as r
import render_antd as antd


def app(_):
    node_id = 0
    nodes = {}

    def generate_nodes() -> List[Dict]:
        nonlocal node_id, nodes
        result = []
        for i in range(3):
            is_leaf = i < 1
            data = {
                "key": f"{node_id}",
                "title": "Tree Node" if is_leaf else "Expand to load",
                "isLeaf": is_leaf,
            }
            nodes[f"{node_id}"] = data
            node_id += 1
            result.append(data)
        return result

    async def load_data(current_node_id: str):
        await asyncio.sleep(0.5)
        nodes[current_node_id]["children"] = generate_nodes()
        treeData.notify()

    treeData = r.ObservableList(generate_nodes())
    return antd.Tree(
        style={"width": "100%"},
        loadData=load_data,
        treeData=treeData,
        onSelect=print,
    )
