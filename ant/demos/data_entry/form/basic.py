import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Form(
        [
            antd.Form.Item(
                antd.Input(),
                label="Username",
                name="username",
                rules=[dict(required=True, message="Please input your username")],
            ),
            antd.Form.Item(
                antd.Input.Password(),
                label="Password",
                name="password",
                rules=[dict(required=True, message="Please input your password!")],
            ),
            antd.Form.Item(
                antd.Checkbox("Remember me"), name="remember", valuePropName="checked"
            ),
            antd.Form.Item(antd.Button("Submit", type="primary", htmlType="submit")),
        ],
        name="basic",
        initialValues=dict(remember=True),
        labelCol=dict(span=8),
        wrapperCol=dict(span=16),
        onFinish=r.Callback(lambda values: print("Success", values)),
        onFinishFailed=r.Callback(lambda values: print("Failed", values)),
    )
