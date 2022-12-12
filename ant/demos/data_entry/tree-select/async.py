import asyncio
import itertools
import pprint

import reflect as r
import reflect_antd as antd

initialTreeData = [
    {"id": 0, "pId": 0, "value": 0, "key": 0, "title": "Expand to load"},
    {"id": 1, "pId": 0, "value": 1, "key": 1, "title": "Expand to load"},
    {"id": 2, "pId": 0, "value": 2, "key": 2, "title": "Tree Node", "isLeaf": True},
]


def app():
    counter = itertools.count(3)
    treeData = r.create_observable(initialTreeData, key="initialTreeData")

    r.autorun(lambda: pprint.pprint(treeData()))

    async def onLoadData1(node_index):
        await asyncio.sleep(0.5)
        value = next(counter)
        treeData()[node_index[0]]["children"] = [
            {
                "id": 3,
                "pId": 0,
                "value": f"child {value}",
                "key": value,
                "title": f"child {value}",
                "isLeaf": True,
            }
        ]
        treeData.touch()

    return antd.TreeSelect(
        style=dict(width="100%"),
        dropdownStyle=dict(maxHeight=400, overflow="auto"),
        placeholder="Please select",
        loadData=r.Callback(onLoadData1, args=("id",), is_promise=True),
        treeData=treeData,
    )
