from render_html import *
from render_antd import Form, Input, Button, Radio
from render_ant_icons import InfoCircleOutlined


def app():
    return Form(
        [
            Form.Item(
                Radio.Group(
                    [
                        Radio.Button("Optional", value="optional"),
                        Radio.Button("Required", value=True),
                        Radio.Button("Hidden", value=False),
                    ]
                ),
                label="Required Mark",
                name="requiredMark",
            ),
            Form.Item(
                Input(placeholder="input placeholder"),
                label="Field A",
                required=True,
                tooltip="This is a required field",
            ),
            Form.Item(
                Input(placeholder="input placeholder"),
                label="Field B",
                tooltip=dict(
                    title="Tooltip with customize icon", icon=InfoCircleOutlined()
                ),
            ),
            Form.Item(Button("Submit", type="primary")),
        ],
        form=form,
        layout="vertical",
        onValuesChange=onRequiredTypeChange,
        requiredMark=requiredMark,
    )
