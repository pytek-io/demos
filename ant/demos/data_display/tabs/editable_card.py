import itertools

import reflect as r
import reflect.utils as reflect_utils
import reflect_antd as antd
import reflect_html as html
JS_MODULES = ["ant_demo"]
TabPane = antd.Tabs.TabPane
initial_panes = [
    ({"tab": "Tab 1", "key": "1"}, "Content of Tab 1"),
    ({"tab": "Tab 2", "key": "2"}, "Content of Tab 2"),
    ({"tab": "Tab 3", "key": "3", "closable": False}, "Content of Tab 3"),
]


def app():
    panes = r.create_observable(initial_panes, key="panes")
    active_key = r.create_observable(0, key="active_key")
    r.autoprint(active_key)
    counter = itertools.count(len(panes()) + 1)

    def onEdit(action, maybe_key):
        if action == "remove":
            index = reflect_utils.find_index(
                panes, lambda pane: pane[0]["key"] == maybe_key
            )
            panes.pop(index)
        else:
            assert action == "add"
            key = str(next(counter))
            panes.append(({"tab": f"Tab {key}", "key": key}, f"Content of Tab {key}"))
            active_key.set(key)

    return antd.Tabs(
        lambda: [TabPane(content, **pane) for pane, content in panes()],
        type="editable-card",
        activeKey=active_key,
        onEdit=r.Callback(onEdit, "onEdit", args=None, multiple_results=True),
    )
