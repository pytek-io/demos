import reflect_antd as antd
import reflect_html as html


def app():
    def confirm():
        print("confirmed")
        antd.message.success("Clicked on Yes")

    def cancel():
        print("cancelled")
        antd.message.error("Clicked on No")

    return antd.Popconfirm(
        html.a("Delete", href="#"),
        title="Are you sure to delete this task?",
        onConfirm=confirm,
        onCancel=cancel,
        okText="Yes",
        cancelText="No",
    )
