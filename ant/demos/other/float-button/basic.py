import reflect_antd as antd


def app():
    return antd.FloatButton(onClick=lambda: print("click"))