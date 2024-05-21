import asyncio

import render as r
import render_antd as antd

message_success = r.js_arrow("message_success", "render_antd.message.success")
message_loading = r.js_arrow("message_loading", "render_antd.message.loading")


def openMessage(window: r.Window):
    async def result():
        key = "something unique"
        first_success_delay = 2.5
        window.call_js_method(
            message_loading({"content": "Action in progress...", "key": key})
        )
        await asyncio.sleep(first_success_delay)
        window.call_js_method(
            message_success(
                {
                    "content": "Loading finished!",
                    "key": key,
                    "duration": first_success_delay + 1,
                }
            )
        )
        await asyncio.sleep(first_success_delay)
        window.call_js_method(
            message_success(
                {"content": "Hurray!", "key": key, "duration": 1}
            )
        )

    return result


def app(window: r.Window):
    return antd.Button("Display sequential messages", onClick=openMessage(window))
