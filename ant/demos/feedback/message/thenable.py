import asyncio

import render as r
import render_antd as antd
import render_html as html


async def openMessage():
    key = "something unique"
    first_success_delay = 2.5
    antd.message.loading({"content": "Action in progress...", "key": key})
    await asyncio.sleep(2.5)
    antd.message.success(
        {
            "content": "Loading finished!",
            "key": key,
            "duration": first_success_delay + 1,
        }
    )
    await asyncio.sleep(first_success_delay)
    antd.message.success(
        {"content": "Loading finished is finished!", "key": key, "duration": 1}
    )


def app():
    return antd.Button("Display sequential messages", onClick=openMessage)
