import render as r
import render_antd as antd


def app(_):
    switch = antd.Switch(defaultChecked=True)
    r.autorun(lambda: print(f"switched to {switch()}"))
    return switch
