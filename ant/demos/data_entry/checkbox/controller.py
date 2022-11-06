from reflect import autorun, create_observable
from reflect_antd import Button, Checkbox
from reflect_html import *
from reflect_utils import toggle_observable


def app():
    disabled = create_observable(False)
    checked = create_observable(True)
    check_box = Checkbox(
        lambda: f"{'Checked' if checked() else  'Unchecked'} - {'Disabled' if disabled() else 'Enabled'}",
        checked=checked,
        disabled=disabled,
    )
    autorun(lambda: print(f"{check_box()}"))
    return div(
        [
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
                        onClick=toggle_observable(checked),
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
    )
