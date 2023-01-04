import reflect as r
import reflect_antd as antd
import reflect_html as html
import reflect_utils


def app():
    disabled = r.ObservableValue(True)
    radio_group1 = antd.Radio("Disabled", defaultChecked=False, disabled=disabled)
    radio_group2 = antd.Radio("Disabled", defaultChecked=True, disabled=disabled)
    return html.div(
        [
            radio_group1,
            radio_group2,
            html.br(),
            antd.Button(
                "Toggle disabled",
                type="primary",
                onClick=reflect_utils.toggle_observable(disabled),
                style=dict(marginTop=16),
            ),
        ]
    )
