from reflect_html import *
from reflect_antd import Popconfirm, message


def app():
    def confirm():
        print("confirmed")
        message.success("Clicked on Yes")

    def cancel():
        print("cancelled")
        message.error("Clicked on No")

    return Popconfirm(
        a("Delete", href="#"),
        title="Are you sure to delete this task?",
        onConfirm=confirm,
        onCancel=cancel,
        okText="Yes",
        cancelText="No",
    )
