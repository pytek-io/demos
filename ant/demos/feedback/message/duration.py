import render_antd as antd
import render as r

message_success = r.js_arrow("message_success", "render_antd.message.success")


def success(window: r.Window):
    def result():
        window.call_js_method(
            message_success(
                "This is a prompt message for success, and it will disappear in 10 seconds",
                10,
            )
        )

    return result


def app(window: r.Window):
    return antd.Button("Customized display duration", onClick=success(window))
