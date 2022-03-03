from reflect_html import *
from reflect_antd import Checkbox

from reflect import autorun


def app():
    check_box = Checkbox("Check me!", defaultChecked=True)
    autorun(lambda: print(f"checked {check_box()}"))
    return check_box