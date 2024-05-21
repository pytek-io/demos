import render_antd as antd
import render as r


message_success = r.js_arrow("message_success", "render_antd.message.success")


def info(window: r.Window):
    def result():
        window.call_js_method(message_success(("This is a normal message")))

    return result


def app(window: r.Window):
    return antd.Button("Display normal message", type="primary", onClick=info(window))
