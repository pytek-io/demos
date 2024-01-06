import asyncio

import render as r
import render_antd as antd
import render_html as html


def app():
    visible = r.ObservableValue(False)
    confirmLoading = r.ObservableValue(False)
    modal_text = r.ObservableValue("Content of the modal")

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
                open=visible,
                onOk=handleOk,
                confirmLoading=confirmLoading,
                onCancel=handleCancel,
            ),
        ]
    )
