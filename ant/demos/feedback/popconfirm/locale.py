from reflect_html import *
from reflect_antd import Popconfirm



def app():
    def handleOk():
        print("Done")

    def handleCancel():
        print("Cancelled")

    return Popconfirm(
        a("Delete", href="#"),
        title="Are you sure？",
        okText="Yeah",
        cancelText="Neah",
        onConfirm=handleOk,
        onCancel=handleCancel,
    )
