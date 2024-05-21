import render_antd as antd
import render as r

message_success = r.js_arrow("message_success", "render_antd.message.success")


def success(window: r.Window):
    def result():
        window.call_js_method(
            message_success(
                {
                    "content": "This is a prompt message with custom className and style",
                    "className": "custom-class",
                    "style": {"marginTop": "20vh"},
                }
            )
        )

    return result


def app(window: r.Window):
    return antd.Button("Customized style", onClick=success(window))
