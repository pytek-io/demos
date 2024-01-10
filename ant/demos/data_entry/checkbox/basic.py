import render as r
import render_antd as antd


def app(_):
    check_box = antd.Checkbox("Check me!", defaultChecked=True)
    r.autorun(lambda: print(f"checked {check_box()}"))
    return check_box
