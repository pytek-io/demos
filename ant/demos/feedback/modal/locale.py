from reflect_html import *
from reflect_antd import Modal, Button, Space
from reflect_ant_icons import ExclamationCircleOutlined
from reflect import make_observable


def confirm():
    Modal.confirm(
        {
            "title": "Confirm",
            "icon": ExclamationCircleOutlined(),
            "content": "Bla bla ...",
            "okText": "确认",
            "cancelText": "取消",
        }
    )


def app():
    visible = make_observable(False)
    return Space(
        [
            Button("Modal", type="primary", onClick=lambda: visible.set(True)),
            Modal(
                [p("Bla bla ..."), p("Bla bla ..."), p("Bla bla ...")],
                title="Modal",
                visible=visible,
                onOk=lambda: visible.set(False),
                onCancel=lambda: visible.set(False),
                okText="确认",
                cancelText="取消",
            ),
            Button("Confirm", onClick=confirm),
        ]
    )
