from render_antd import Button, Modal
from render_html import *

visible, loading = this.visible, this.loading


def app(_):
    return [
        Button(
            "Open Modal with customized footer", type="primary", onClick=this.showModal
        ),
        Modal(
            "Return",
            visible=visible,
            title="Title",
            onOk=this.handleOk,
            onCancel=this.handleCancel,
            footer=Button(keyback=True, onClick=this.handleCancel),
        ),
        Button(
            "Submit",
            key="submit",
            type="primary",
            loading=loading,
            onClick=this.handleOk,
        ),
        p("Some contents..."),
        p("Some contents..."),
        p("Some contents..."),
        p("Some contents..."),
        p("Some contents..."),
    ]
