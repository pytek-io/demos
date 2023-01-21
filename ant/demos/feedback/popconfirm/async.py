import reflect as r
import reflect_antd as antd


def app():
    visible = r.ObservableValue(False)
    confirmLoading = r.ObservableValue(False)

    def showPopconfirm():
        visible.set(True)

    def deferred():
        visible.set(False)
        confirmLoading.set(False)

    def handleOk():
        confirmLoading.set(True)
        r.schedule_callback(2, deferred)

    def handleCancel():
        print("Clicked cancel button")
        visible.set(False)

    return antd.Popconfirm(
        antd.Button(
            "Open Popconfirm with async logic", type="primary", onClick=showPopconfirm
        ),
        title="Title",
        open=visible,
        onConfirm=handleOk,
        okButtonProps=lambda: {"loading": confirmLoading()},
        onCancel=handleCancel,
    )
