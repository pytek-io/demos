from reflect_html import *
from reflect_antd import Spin, Switch, Alert
from reflect import autorun

def app():
    loading = Switch(defaultChecked=False)
    return div(
        [
            Spin(
                Alert(
                    message="Alert message title",
                    description="Further details about the context of this alert.",
                    type="info",
                ),
                spinning=loading,
            ),
            div(
                [
                    "Loading state：",
                    loading,
                ],
                style=dict(marginTop=16),
            ),
        ]
    )
