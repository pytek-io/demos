import render_antd as antd


def app(_):
    return antd.FloatButton(onClick=lambda: print("click"))
