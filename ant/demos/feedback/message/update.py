import asyncio

import render as r
import render_antd as antd


message_success = r.js_arrow("message_success", "render_antd.message.success")
message_loading = r.js_arrow("message_loading", "render_antd.message.loading")


def openMessage(window: r.Window):
    async def result():
        key = "something unique"
        window.call_js_method(
            message_loading({"content": "Action in progress...", "key": key})
        )
        await asyncio.sleep(1)
        window.call_js_method(
            message_success(
                {
                    "content": "Loaded!",
                    "key": key,
                    "duration": 2,
                }
            )
        )

    return result


def app(window: r.Window):
    return antd.Button(
        "Open the message box", type="primary", onClick=openMessage(window)
    )
