from reflect_html import *
from reflect_antd import Form, Input, Button, Checkbox
from reflect import Callback


def app():
    return Form(
        [
            Form.Item(
                Input(),
                label="Username",
                name="username",
                rules=[dict(required=True, message="Please input your username")],
            ),
            Form.Item(
                Input.Password(),
                label="Password",
                name="password",
                rules=[dict(required=True, message="Please input your password!")],
            ),
            Form.Item(
                Checkbox("Remember me"), name="remember", valuePropName="checked"
            ),
            Form.Item(Button("Submit", type="primary", htmlType="submit")),
        ],
        name="basic",
        initialValues=dict(remember=True),
        labelCol=dict(span=8),
        wrapperCol=dict(span=16),
        onFinish=Callback(
            lambda values: print("Success", values)
        ),
        onFinishFailed=Callback(
            lambda values: print("Failed", values)
        ),
    )
