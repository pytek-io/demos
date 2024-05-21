import render_antd as antd
import render as r


message_success = r.js_arrow("message_success", "render_antd.message.success")
message_error = r.js_arrow("message_error", "render_antd.message.error")
message_warning = r.js_arrow("message_warning", "render_antd.message.warning")


def create_callback(
    window: r.Window, message_method, message: str = None, duration: int = 5
):
    def result():
        window.call_js_method(message_method(message, duration))

    return result


def app(window: r.Window):
    return antd.Space(
        [
            antd.Button(
                "Success",
                onClick=create_callback(
                    window, message_success, "This is a success message"
                ),
            ),
            antd.Button(
                "Error",
                onClick=create_callback(
                    window, message_error, "This is an error message"
                ),
            ),
            antd.Button(
                "Warning",
                onClick=create_callback(
                    window, message_warning, "This is a warning message"
                ),
            ),
        ]
    )
