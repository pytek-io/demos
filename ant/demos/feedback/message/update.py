import asyncio

import render as r
import render_antd as antd
import render_html as html


async def openMessage():
    key = "something unique"
    antd.message.loading({"content": "Loading...", "key": key})
    await asyncio.sleep(1)
    antd.message.success({"content": "Loaded!", "key": key, "duration": 2})


def app(_):
    return antd.Button("Open the message box", type="primary", onClick=openMessage)
