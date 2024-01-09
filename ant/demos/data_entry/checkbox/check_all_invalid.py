import render as r
import render_antd as antd
import render_html as html

PLAIN_OPTIONS = ["Apple", "Pear", "Orange"]
DEFAULT_CHECKED_LIST = ["Apple", "Orange"]


def app():
    checked = r.ObservableValue(False)
    def check_all(args):
        print(args)
        checked.set(checked_list() and len(checked_list()) == len(PLAIN_OPTIONS))

    checked_list = antd.Checkbox.Group(
        options=PLAIN_OPTIONS, defaultValue=DEFAULT_CHECKED_LIST, onChange=check_all
    )
    indeterminate = lambda: bool(checked_list() and len(checked_list()) > 0)


    r.autoprint(checked_list)
    r.autoprint(indeterminate)

    def onCheckAllChange(value):
        checked_list.set(PLAIN_OPTIONS if value else [])
        indeterminate.set(False)

    return html.div(
        [
            antd.Checkbox("Check all", indeterminate=indeterminate, checked=checked),
            antd.Divider(),
            checked_list,
        ]
    )
