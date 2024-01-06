import render_antd as antd
import render_html as html


def success():
    antd.message.success("This is a success message")


def error():
    antd.message.error("This is an error message")


def warning():
    antd.message.warning("This is a warning message")


def app():
    return antd.Space(
        [
            antd.Button("Success", onClick=success),
            antd.Button("Error", onClick=error),
            antd.Button("Warning", onClick=warning),
        ]
    )
