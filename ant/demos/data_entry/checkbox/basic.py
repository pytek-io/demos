import reflect_antd as antd

import reflect as r


def app():
    check_box = antd.Checkbox("Check me!", defaultChecked=True)
    r.autorun(lambda: print(f"checked {check_box()}"))
    return check_box
