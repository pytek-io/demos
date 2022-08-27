from reflect_html import *
from reflect_antd import Tabs
from reflect import create_observable, autorun
from reflect.utils import find_index
from reflect import Callback
from itertools import count

TabPane = Tabs.TabPane


initial_panes = [
    (
        {"tab": "Tab 1", "key": "1"},
        "Content of Tab 1",
    ),
    ({"tab": "Tab 2", "key": "2"}, "Content of Tab 2"),
]


def app():
    panes = create_observable(initial_panes, key="panes")
    active_key = create_observable(initial_panes[0][0]["key"], key="active_key")
    autorun(lambda: print(active_key()))
    counter = count(len(panes()) + 1)

    def onEdit(action, maybe_key):
        if action == "remove":
            panes.pop(
                find_index(panes(), lambda pane: pane[0]["key"] == maybe_key)
            )
        else:
            assert action == "add"
            key = str(next(counter))
            panes.append(({"tab": f"Tab {key}", "key": key}, f"Content of Tab {key}"))
            active_key.set(key)

    return Tabs(
        lambda: [TabPane(content, **pane) for pane, content, in panes()],
        type="editable-card",
        onChange=Callback(active_key.set),
        activeKey=active_key,
        onEdit=Callback(onEdit, "onEdit", multiple_results=True),
    )
