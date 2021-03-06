from reflect import make_observable
from reflect_antd import Button, InputNumber
from reflect_html import *
from reflect_utils.common import toggle_observable


def app():
    disabled = make_observable(True)
    return div([
        InputNumber(min=1, max=10, disabled=disabled, defaultValue=3),
        div(
            Button("Toggle disabled", onClick=toggle_observable(disabled), type="primary"),
            style=dict(marginTop=20),
        ),
    ])
