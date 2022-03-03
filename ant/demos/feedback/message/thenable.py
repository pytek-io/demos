from reflect_html import *
from reflect_antd import message, Button
from reflect import schedule_callback
from asyncio import sleep


async def openMessage():
    key = "something unique"
    first_success_delay = 2.5
    message.loading({"content": "Action in progress...", "key": key})
    await sleep(2.5)
    # rmk: we make the duration sligthly longer to be sure the message window won't close and reopen
    message.success(
        {
            "content": "Loading finished!",
            "key": key,
            "duration": first_success_delay + 1,
        }
    )
    await sleep(first_success_delay)
    message.success(
        {
            "content": "Loading finished is finished!",
            "key": key,
            "duration": 1,
        }
    )


def app():
    return Button("Display sequential messages", onClick=openMessage)
