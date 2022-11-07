import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    visible = r.create_observable(False)
    confirmLoading = r.create_observable(False)

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
        visible=visible,
        onConfirm=handleOk,
        okButtonProps=dict(loading=confirmLoading),
        onCancel=handleCancel,
    )
