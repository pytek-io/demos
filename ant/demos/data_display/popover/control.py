import render_antd as antd
import render as r


def app():
    visible = r.ObservableValue(False)
    return antd.Popover(
        antd.Button("Click me", type="primary", onClick=visible.toggle),
        title="Title",
        visible=visible,
    )
