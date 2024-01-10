import itertools

import render as r
import render_antd as antd

from demos.ant.demos.utils import find_index

initial_panes = [
    {"label": "Tab 1", "key": "1", "children": "Content of Tab 1"},
    {"label": "Tab 2", "key": "2", "children": "Content of Tab 2"},
]


def app(_):
    panes = r.create_observable(initial_panes.copy(), key="panes")
    active_key = r.create_observable(initial_panes[0]["key"], key="active_key")
    r.autorun(lambda: print(active_key()))
    counter = itertools.count(len(panes()) + 1)

    def onEdit(action, maybe_key):
        if action == "remove":
            panes.pop(find_index(panes(), lambda pane: pane[0]["key"] == maybe_key))
        else:
            assert action == "add"
            key = str(next(counter))
            panes.append(({"tab": f"Tab {key}", "key": key}, f"Content of Tab {key}"))
            active_key.set(key)

    return antd.Tabs(
        items=initial_panes,
        type="editable-card",
        onChange=r.Callback(active_key.set),
        activeKey=active_key,
        # onEdit=r.Callback(onEdit, "onEdit", multiple_results=True),
    )
