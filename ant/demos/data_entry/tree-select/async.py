from asyncio import sleep
from itertools import count

from reflect import Callback
from reflect import autorun, create_observable
from reflect_antd import TreeSelect

initialTreeData = [
    {"id": 0, "pId": 0, "value": 0, "key": 0, "title": "Expand to load"},
    {"id": 1, "pId": 0, "value": 1, "key": 1, "title": "Expand to load"},
    {"id": 2, "pId": 0, "value": 2, "key": 2, "title": "Tree Node", "isLeaf": True},
]


def app():
    counter = count(3)
    treeData = create_observable(initialTreeData, key="initialTreeData")
    import pprint

    autorun(lambda: pprint.pprint((treeData())))

    async def onLoadData(node_index):
        await sleep(0.5)
        value = next(counter)
        treeData()[node_index]["children"] = [
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

    return TreeSelect(
        style=dict(width="100%"),
        dropdownStyle=dict(maxHeight=400, overflow="auto"),
        placeholder="Please select",
        loadData=Callback(onLoadData, "id", is_promise=True),
        treeData=treeData,
    )
