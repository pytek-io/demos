import render as r
import render_antd as antd
import render_html as html
import render_utils


def app(_):
    disabled = r.ObservableValue(True)
    return html.div(
        [
            antd.InputNumber(min=1, max=10, disabled=disabled, defaultValue=3),
            html.div(
                antd.Button(
                    "Toggle disabled",
                    onClick=render_utils.toggle_observable(disabled),
                    type="primary",
                ),
                style={"marginTop": 20},
            ),
        ]
    )
