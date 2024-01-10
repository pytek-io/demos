from asyncio import sleep

from render_antd import Button, message
from render_html import *


async def success():
    key = "something unique"
    hide = await execute(message.loading, {"content": "Action in progress...", "key": key, "duration": 0})
    await sleep(2.5)
    hide()


def app(_):
    raise not NotImplementedError()
    return Button("Display a loading indicator", onClick=success)
