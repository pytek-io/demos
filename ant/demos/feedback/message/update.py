from reflect_html import *
from reflect_antd import Button, message
from reflect import schedule_callback
from asyncio import sleep


async def openMessage():
    key = "something unique"
    message.loading({"content": "Loading...", "key": key})
    await sleep(1)
    message.success({"content": "Loaded!", "key": key, "duration": 2})


def app():
    return Button("Open the message box", type="primary", onClick=openMessage)
