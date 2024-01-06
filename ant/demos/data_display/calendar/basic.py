import render_antd as antd


def app():
    return antd.Calendar(onPanelChange=print)
