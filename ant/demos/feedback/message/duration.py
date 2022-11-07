import reflect_antd as antd
import reflect_html as html


def success():
    antd.message.success(
        "This is a prompt message for success, and it will disappear in 10 seconds", 10
    )


def app():
    return antd.Button("Customized display duration", onClick=success)
