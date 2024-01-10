import render as r
import render_antd as antd
import render_html as html

PLAIN_OPTIONS = ["Apple", "Pear", "Orange"]
OPTIONS = [
    {"label": "Apple", "value": "Apple"},
    {"label": "Pear", "value": "Pear"},
    {"label": "Orange", "value": "Orange"},
]
OPTIONS_WITH_DISABLED = [
    {"label": "Apple", "value": "Apple"},
    {"label": "Pear", "value": "Pear"},
    {"label": "Orange", "value": "Orange", "disabled": False},
]


def app(_):
    check_box1 = antd.Checkbox.Group(options=PLAIN_OPTIONS, defaultValue=["Apple"])
    check_box2 = antd.Checkbox.Group(options=OPTIONS, defaultValue=["Pear"])
    check_box3 = antd.Checkbox.Group(
        options=OPTIONS_WITH_DISABLED, disabled=True, defaultValue=["Apple"]
    )
    r.autorun(lambda: print("checked values", check_box1()))
    r.autorun(lambda: print("checked values", check_box2()))
    r.autorun(lambda: print("checked values", check_box3()))
    return html.div(
        [check_box1, html.br(), html.br(), check_box2, html.br(), html.br(), check_box3]
    )
