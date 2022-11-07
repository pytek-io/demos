import asyncio

import reflect as r
import reflect_antd as antd
import reflect_html as html


async def openMessage():
    key = "something unique"
    antd.message.loading({"content": "Loading...", "key": key})
    await asyncio.sleep(1)
    antd.message.success({"content": "Loaded!", "key": key, "duration": 2})


def app():
    return antd.Button("Open the message box", type="primary", onClick=openMessage)
