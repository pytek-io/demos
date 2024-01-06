import render_antd as antd
import render_html as html


def app():
    def handleOk():
        print("Done")

    def handleCancel():
        print("Cancelled")

    return antd.Popconfirm(
        html.a("Delete", href="#"),
        title="Are you sure？",
        okText="Yeah",
        cancelText="Neah",
        onConfirm=handleOk,
        onCancel=handleCancel,
    )
