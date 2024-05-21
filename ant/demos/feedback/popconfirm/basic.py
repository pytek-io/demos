import render_antd as antd


def app(_):
    def confirm():
        print("confirmed")
        antd.message.success("Clicked on Yes")

    def cancel():
        print("cancelled")
        antd.message.error("Clicked on No")

    return antd.Popconfirm(
        antd.Button("Delete"),
        title="Are you sure to delete this task?",
        onConfirm=confirm,
        onCancel=cancel,
        okText="Yes",
        cancelText="No",
    )
