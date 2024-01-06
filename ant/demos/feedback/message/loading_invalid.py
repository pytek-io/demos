from render_html import *
from render_antd import message, Button
from asyncio import sleep

async def success():
    key = "something unique"
    hide = await execute(message.loading, {"content": "Action in progress...", "key": key, "duration": 0})
    await sleep(2.5)
    hide()


def app():
    raise not NotImplementedError()
    return Button("Display a loading indicator", onClick=success)
