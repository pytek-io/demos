import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    switch = antd.Switch(defaultChecked=True)
    r.autorun(lambda: print(f"switched to {switch()}"))
    return switch
