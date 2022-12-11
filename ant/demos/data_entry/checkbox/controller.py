import reflect_antd as antd
import reflect_html as html
import reflect_utils

import reflect as r


def app():
    disabled = r.create_observable(False)
    checked = r.create_observable(True)
    check_box = antd.Checkbox(
        lambda: f"{'Checked' if checked() else 'Unchecked'} - {'Disabled' if disabled() else 'Enabled'}",
        checked=checked,
        disabled=disabled,
    )
    r.autorun(lambda: print(f"{check_box()}"))
    return html.div(
        [
            html.p(check_box, style=dict(marginBottom="20px")),
            html.p(
                [
                    antd.Button(
                        lambda: "Check" if checked() else "Uncheck",
                        type="primary",
                        size="small",
                        onClick=reflect_utils.toggle_observable(checked),
                    ),
                    antd.Button(
                        lambda: "Enable" if disabled() else "Disable",
                        style=dict(margin="0 10px"),
                        type="primary",
                        size="small",
                        onClick=reflect_utils.toggle_observable(disabled),
                    ),
                ]
            ),
        ]
    )
