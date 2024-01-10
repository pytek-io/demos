import render_antd as antd
import render_html as html


def info():
    print("calling info")
    antd.Modal.info(
        {
            "title": "This is a notification message",
            "content": html.div(
                [
                    html.p("some messages...some messages..."),
                    html.p("some messages...some messages..."),
                ]
            ),
        }
    )


def success():
    antd.Modal.success({"content": "some messages...some messages..."})


def error():
    antd.Modal.error(
        {
            "title": "This is an error message",
            "content": "some messages...some messages...",
        }
    )


def warning():
    antd.Modal.warning(
        {
            "title": "This is a warning message",
            "content": "some messages...some messages...",
        }
    )


def app(_):
    return antd.Space(
        [
            antd.Button("Info", onClick=info),
            antd.Button("Success", onClick=success),
            antd.Button("Error", onClick=error),
            antd.Button("Warning", onClick=warning),
        ]
    )
