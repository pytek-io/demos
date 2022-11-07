from reflect import create_observable
from reflect_antd import Button, Radio
from reflect_html import *
from reflect_utils import toggle_observable


def app():
    disabled = create_observable(True)
    radio_group1 = Radio("Disabled", defaultChecked=False, disabled=disabled)
    radio_group2 = Radio("Disabled", defaultChecked=True, disabled=disabled)
    return div(
        [
            radio_group1,
            radio_group2,
            br(),
            Button(
                "Toggle disabled",
                type="primary",
                onClick=toggle_observable(disabled),
                style=dict(marginTop=16),
            ),
        ]
    )
