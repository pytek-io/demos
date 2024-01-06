import render as r
import render_antd as antd
import render_html as html
import render_utils


def app():
    disabled = r.ObservableValue(False)
    checked = r.ObservableValue(True)
    check_box = antd.Checkbox(
        lambda: f"{'Checked' if checked() else 'Unchecked'} - {'Disabled' if disabled() else 'Enabled'}",
        checked=checked,
        disabled=disabled,
    )
    r.autorun(lambda: print(f"{check_box()}"))
    return html.div(
        [
            html.p(check_box, style={"marginBottom": "20px"}),
            html.p(
                [
                    antd.Button(
                        lambda: "Check" if checked() else "Uncheck",
                        type="primary",
                        size="small",
                        onClick=render_utils.toggle_observable(checked),
                    ),
                    antd.Button(
                        lambda: "Enable" if disabled() else "Disable",
                        style={"margin": "0 10px"},
                        type="primary",
                        size="small",
                        onClick=render_utils.toggle_observable(disabled),
                    ),
                ]
            ),
        ]
    )
