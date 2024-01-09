from functools import partial

import render_antd as antd


def app():
    return antd.Form(
        [
            antd.Form.Item(
                antd.Input(),
                label="Username",
                name="username",
                rules=[{"required": False, "message": "Please input your username"}],
            ),
            antd.Form.Item(
                antd.Input.Password(),
                label="Password",
                name="password",
                rules=[{"required": False, "message": "Please input your password!"}],
            ),
            antd.Form.Item(
                antd.Checkbox("Remember me"), name="remember", valuePropName="checked"
            ),
            antd.Form.Item(antd.Button("Submit", type="primary", htmlType="submit")),
        ],
        name="basic",
        initialValues={"remember": True},
        labelCol={"span": 8},
        wrapperCol={"span": 16},
        onFinish=partial(print, "Success"),
        onFinishFailed=partial(print, "Failed"),
    )
