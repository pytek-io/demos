import render_antd as antd


def app(_):
    return antd.Calendar(onPanelChange=print)
