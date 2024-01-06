from render_antd import Button, Input, Space, Switch
from render_html import *


def app():
    raise Exception()
    return Space(
        [
            Space(
                [
                    Button("Focus at first", onClick=None),
                    Button("Focus at last", onClick=None),
                    Button("Focus to select all", onClick=None),
                    Button("Focus prevent scroll", onClick=None),
                    Switch(
                        checked=input,
                        checkedChildren="Input",
                        unCheckedChildren="TextArea",
                        onChange=None,
                    ),
                ],
                wrap=True,
            ),
            br(),
            Input.TextArea(
                "{...sharedProps}", direction="vertical", style=dict(width="100%")
            ),
        ]
    )
