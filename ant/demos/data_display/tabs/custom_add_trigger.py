import itertools

import reflect as r
import reflect_antd as antd
import reflect_html as html

from demos.ant.demos.utils import find_index

TabPane = antd.Tabs.TabPane
initial_panes = [
    ({"tab": "Tab 1", "key": "1"}, "Content of Tab 1"),
    ({"tab": "Tab 2", "key": "2"}, "Content of Tab 2"),
]


def app():
    panes = r.create_observable(initial_panes, key="panes")
    active_key = r.create_observable(initial_panes[0][0]["key"], key="active_key")
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
        lambda: [TabPane(content, **pane) for pane, content in panes()],
        type="editable-card",
        onChange=r.Callback(active_key.set),
        activeKey=active_key,
        onEdit=r.Callback(onEdit, "onEdit", multiple_results=True),
    )
