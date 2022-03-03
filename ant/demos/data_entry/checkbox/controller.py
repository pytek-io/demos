from reflect import autorun, make_observable
from reflect_antd import Button, Checkbox
from reflect_html import *
from reflect_utils.common import toggle_observable


def app():
    disabled = make_observable(False)
    checked = make_observable(True)
    check_box = Checkbox(
        lambda: f"{'Checked' if checked() else  'Unchecked'} - {'Disabled' if disabled() else 'Enabled'}",
        checked=checked,
        disabled=disabled,
    )
    autorun(lambda: print(f"{check_box()=}"))
    return [
        p(
            check_box,
            style=dict(marginBottom="20px"),
        ),
        p(
            [
                Button(
                    lambda: "Check" if checked() else "Uncheck",
                    type="primary",
                    size="small",
                    onClick=toggle_observable(check_box.checked),
                ),
                Button(
                    lambda: "Enable" if disabled() else "Disable",
                    style=dict(margin="0 10px"),
                    type="primary",
                    size="small",
                    onClick=toggle_observable(disabled),
                ),
            ]
        ),
    ]
