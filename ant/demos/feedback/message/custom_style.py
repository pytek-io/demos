import render_antd as antd
import render_html as html


def success():
    antd.message.success(
        {
            "content": "This is a prompt message with custom className and style",
            "className": "custom-class",
            "style": {"marginTop": "20vh"},
        }
    )


def app(_):
    return antd.Button("Customized style", onClick=success)
