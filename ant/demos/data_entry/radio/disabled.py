import render as r
import render_antd as antd
import render_html as html
import render_utils


def app(_):
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
                onClick=render_utils.toggle_observable(disabled),
                style={"marginTop": 16},
            ),
        ]
    )
