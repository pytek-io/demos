from itertools import count

from reflect import autorun, make_observable
from reflect import Callback
from reflect.utils import find_index
from reflect_antd import Tabs
from reflect_html import *

TabPane = Tabs.TabPane


initial_panes = [
    (
        {"tab": "Tab 1", "key": "1"},
        "Content of Tab 1",
    ),
    ({"tab": "Tab 2", "key": "2"}, "Content of Tab 2"),
    (
        {
            "tab": "Tab 3",
            "key": "3",
            "closable": False,
        },
        "Content of Tab 3",
    ),
]


def app():
    panes = make_observable(initial_panes, key="panes")
    active_key = make_observable(0, key="active_key")
    autorun(lambda: print(active_key()))
    counter = count(len(panes()) + 1)

    def onEdit(action, maybe_key):
        if action == "remove":
            index = find_index(panes, lambda pane: pane[0]["key"] == maybe_key)
            panes.pop(index)
        else:
            assert action == "add"
            key = str(next(counter))
            panes.append(
                ({"tab": f"Tab {key}", "key": key}, f"Content of Tab {key}")
            )
            active_key.set(key)

    return Tabs(
        lambda: [TabPane(content, **pane) for pane, content, in panes()],
        type="editable-card",
        activeKey=active_key,
        onEdit=Callback(onEdit, "onEdit", multiple_results=True),
    )
