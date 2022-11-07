import asyncio

import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

confirm = antd.Modal.confirm
JS_MODULES = ["ant_demo", "ant-icons"]


def on_ok():
    print("OK")


def on_cancel():
    print("Cancel")


def showConfirm():
    confirm(
        dict(
            title="Do you want to delete these items?",
            icon=ant_icons.ExclamationCircleOutlined(),
            content="Some descriptions",
            onOk=on_ok,
            onCancel=on_cancel,
        )
    )


async def async_ok(argument):
    await asyncio.sleep(1.0)
    raise Exception("Oops something went wrong")


def showPromiseConfirm():
    confirm(
        dict(
            title="Do you want to delete these items?",
            icon=ant_icons.ExclamationCircleOutlined(),
            content="When clicked the OK button, this dialog will be closed after 1 second",
            onOk=async_ok,
        )
    )


def showDeleteConfirm():
    confirm(
        dict(
            title="Are you sure you want to delete this task?",
            icon=ant_icons.ExclamationCircleOutlined(),
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
            icon=ant_icons.ExclamationCircleOutlined(),
            content="Some descriptions",
            okText="Yes",
            okType="danger",
            okButtonProps={"disabled": True},
            cancelText="No",
            onOk=on_ok,
            onCancel=on_cancel,
        )
    )


def app():
    return antd.Space(
        [
            antd.Button("Confirm", onClick=showConfirm),
            antd.Button("With promise", onClick=showPromiseConfirm),
            antd.Button("Delete", onClick=showDeleteConfirm, type="dashed"),
            antd.Button("With extra props", onClick=showPropsConfirm, type="dashed"),
        ]
    )
