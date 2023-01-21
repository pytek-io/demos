import reflect as r
import reflect_antd as antd
import reflect_html as html
import reflect_utils


def app():
    disabled = r.ObservableValue(True)
    return html.div(
        [
            antd.InputNumber(min=1, max=10, disabled=disabled, defaultValue=3),
            html.div(
                antd.Button(
                    "Toggle disabled",
                    onClick=reflect_utils.toggle_observable(disabled),
                    type="primary",
                ),
                style={"marginTop": 20},
            ),
        ]
    )
