from asyncio import sleep

from reflect_ant_icons import ExclamationCircleOutlined
from reflect_antd import Button, Modal, Space
from reflect_html import *

confirm = Modal.confirm

JS_MODULES = ["ant_demo", "ant-icons"]


def on_ok():
    print("OK")


def on_cancel():
    print("Cancel")


def showConfirm():
    confirm(
        dict(
            title="Do you want to delete these items?",
            icon=ExclamationCircleOutlined(),
            content="Some descriptions",
            onOk=on_ok,
            onCancel=on_cancel,
        )
    )


async def async_ok(argument):
    await sleep(1.0)
    # the exception message should appear in the web client console
    raise Exception("Oops something went wrong")


def showPromiseConfirm():
    confirm(
        dict(
            title="Do you want to delete these items?",
            icon=ExclamationCircleOutlined(),
            content="When clicked the OK button, this dialog will be closed after 1 second",
            onOk=async_ok,
        )
    )


def showDeleteConfirm():
    confirm(
        dict(
            title="Are you sure you want to delete this task?",
            icon=ExclamationCircleOutlined(),
            content="Some descriptions",
            okText="Yes",
            okType="danger",
            cancelText="No",
            onOk=on_ok,
            onCancel=on_cancel,
        )
    )


def showPropsConfirm():
    confirm(
        dict(
            title="Are you sure you want to delete this task?",
            icon=ExclamationCircleOutlined(),
            content="Some descriptions",
            okText="Yes",
            okType="danger",
            okButtonProps={
                "disabled": True,
            },
            cancelText="No",
            onOk=on_ok,
            onCancel=on_cancel,
        )
    )


def app():
    return Space(
        [
            Button("Confirm", onClick=showConfirm),
            Button("With promise", onClick=showPromiseConfirm),
            Button("Delete", onClick=showDeleteConfirm, type="dashed"),
            Button("With extra props", onClick=showPropsConfirm, type="dashed"),
        ]
    )
