import render_antd as antd


def app():
    return antd.Calendar(fullscreen=False, onPanelChange=print)
