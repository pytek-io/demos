from reflect_html import *
from reflect_antd import Switch, Checkbox
from reflect import create_observable

# rmk: using a CheckBox instead of a button and an observable as it is more
# idiomatic in many respects
def app():
    check_box = Checkbox("Toggle disabled")
    switch = Switch(disabled=check_box.checked, defaultChecked=True)
    return [switch, br(), check_box]
