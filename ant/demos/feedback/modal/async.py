import asyncio

import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    visible = r.create_observable(False)
    confirmLoading = r.create_observable(False)
    modal_text = r.create_observable("Content of the modal")

    async def handleOk():
        modal_text.set("The modal will be closed after two seconds")
        confirmLoading.set(True)
        await asyncio.sleep(2)
        visible.set(False)
        confirmLoading.set(False)

    async def handleCancel():
        print("Clicked cancel button")
        visible.set(False)

    return html.div(
        [
            antd.Button(
                "Open Modal with async logic",
                type="primary",
                onClick=lambda: visible.set(True),
            ),
            antd.Modal(
                html.p(modal_text),
                title="Title",
                visible=visible,
                onOk=handleOk,
                confirmLoading=confirmLoading,
                onCancel=handleCancel,
            ),
        ]
    )
