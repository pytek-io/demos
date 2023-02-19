import asyncio
from itertools import count
from typing import Dict, List

import pandas as pd
import reflect as r
import reflect_antd as antd
import reflect_html as html

import demos.fred as fred


def sort_nodes(categories):
    return sorted(categories, key=lambda x: x["title"])


def filter_category(row):
    return not any(word in row.name for word in ["County", "District", "East", ", KY"])


def filter_series(row):
    return not any(word in row.title for word in ["(DISCONTINUED)"])


COUNTRIES = [""]


def app():
    node_id = 0
    nodes_by_id = {}
    nodes_by_key = {}
    key = count()

    def create_nodes(category_id, definitions, leaf, formatter, node_filter):
        children = [
            {
                "id": f"{row.id}",
                "key": f"{key_value}",
                "title": formatter(row),
                "isLeaf": leaf,
            }
            for row, key_value in zip(definitions.itertuples(), key)
            if node_filter(row)
        ]
        nodes_by_id.update((child["id"], child) for child in children)
        nodes_by_key.update((child["key"], child) for child in children)
        return sort_nodes(children)

    def generate_nodes(category_id) -> List[Dict]:
        children = fred.get_fred_category_children(category_id)
        if not children.empty:
            return create_nodes(
                category_id,
                children,
                leaf=False,
                formatter=lambda row: f"{row.name}, {row.id}",
                node_filter=filter_category,
            )
        else:
            return create_nodes(
                category_id,
                fred.get_fred_category_series(category_id),
                leaf=True,
                formatter=lambda row: f"{row.title}, {row.id}",
                node_filter=filter_series,
            )

    async def load_data(current_node_id: str):
        nodes_by_id[current_node_id]["children"] = generate_nodes(current_node_id)
        treeData.touch()

    df = pd.read_pickle("demos/categories.pick")
    values = [
        {"title": name, "id": f"{id}", "key": f"{key_value}", "isLeaf": False}
        for (id, name, parent_id), key_value in zip(
            ((row.id, row.name, row.parent_id) for row in df.itertuples()), key
        )
        if not any(word in name for word in ["County", "District", "(DISCONTINUED)"])
    ]
    values = [
        {"title": "Prices", "id": "32455", "key": 32455, "isLeaf": False}
    ] + sort_nodes(values)
    nodes_by_id.update((value["id"], value) for value in values)
    nodes_by_key.update((value["key"], value) for value in values)
    treeData = r.ObservableList(values)
    current_node = r.ObservableValue()

    def on_node_selected(node_key):
        node = nodes_by_key[node_key]
        current_node.set(f"selected {node['name' if 'name' in node else 'title']}")
        print(node_key)

    def description():
        print("called description", current_node())
        return current_node()

    us_regional = antd.Switch(False)
    return antd.Row(
        map(
            lambda x: antd.Col(x, style={"width": "50%"}),
            [
                html.div(
                    antd.Tree(
                        style={"width": "100%", "maxHeight": "100%"},
                        showLine={"showLeafIcon": False},
                        loadData=load_data,
                        treeData=treeData,
                        onSelect=on_node_selected,
                        onRightClick=lambda: print("User right clicked!"),
                    ),
                    style={"overflow": "auto", "maxHeight": "100%"},
                ),
                html.div(description),
            ],
        ),
        style={"height": "100%"},
    )
