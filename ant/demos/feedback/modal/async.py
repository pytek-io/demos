from asyncio import sleep


from reflect_html import *
from reflect import create_observable
from reflect_antd import Button, Modal


def app():
    visible = create_observable(False)
    confirmLoading = create_observable(False)
    modal_text = create_observable("Content of the modal")

    async def handleOk():
        modal_text.set("The modal will be closed after two seconds")
        confirmLoading.set(True)
        await sleep(2)
        visible.set(False)
        confirmLoading.set(False)

    async def handleCancel():
        print("Clicked cancel button")
        visible.set(False)

    return div(
        [
            Button(
                "Open Modal with async logic",
                type="primary",
                onClick=lambda: visible.set(True),
            ),
            Modal(
                p(modal_text),
                title="Title",
                visible=visible,
                onOk=handleOk,
                confirmLoading=confirmLoading,
                onCancel=handleCancel,
            ),
        ]
    )
