from reflect_html import *
from reflect_antd import Popconfirm, Button
from reflect import make_observable
from reflect import schedule_callback


def app():
    visible = make_observable(False)
    confirmLoading = make_observable(False)

    def showPopconfirm():
        visible.set(True)

    def deferred():
        visible.set(False)
        confirmLoading.set(False)

    def handleOk():
        confirmLoading.set(True)
        schedule_callback(2, deferred)

    def handleCancel():
        print("Clicked cancel button")
        visible.set(False)

    return Popconfirm(
        Button(
            "Open Popconfirm with async logic", type="primary", onClick=showPopconfirm
        ),
        title="Title",
        visible=visible,
        onConfirm=handleOk,
        okButtonProps=dict(loading=confirmLoading),
        onCancel=handleCancel,
    )
