import asyncio

import render_ant_icons as ant_icons
import render_antd as antd

confirm = antd.Modal.confirm


def on_ok():
    print("OK")


def on_cancel():
    print("Cancel")


def showConfirm():
    confirm(
        {
            "title": "Do you want to delete these items?",
            "icon": ant_icons.ExclamationCircleOutlined(),
            "content": "Some descriptions",
            "onOk": on_ok,
            "onCancel": on_cancel,
        }
    )


async def async_ok(*argument):
    await asyncio.sleep(1.0)
    print("hello")


def showPromiseConfirm():
    confirm(
        {
            "title": "Do you want to delete these items?",
            "icon": ant_icons.ExclamationCircleOutlined(),
            "content": "When clicked the OK button, this dialog will be closed after 1 second",
            "onOk": async_ok,
        }
    )


def showDeleteConfirm():
    confirm(
        {
            "title": "Are you sure you want to delete this task?",
            "icon": ant_icons.ExclamationCircleOutlined(),
            "content": "Some descriptions",
            "okText": "Yes",
            "okType": "danger",
            "cancelText": "No",
            "onOk": on_ok,
            "onCancel": on_cancel,
        }
    )


def showPropsConfirm():
    confirm(
        {
            "title": "Are you sure you want to delete this task?",
            "icon": ant_icons.ExclamationCircleOutlined(),
            "content": "Some descriptions",
            "okText": "Yes",
            "okType": "danger",
            "okButtonProps": {"disabled": True},
            "cancelText": "No",
            "onOk": on_ok,
            "onCancel": on_cancel,
        }
    )


def app(_):
    return antd.Space(
        [
            antd.Button("Confirm", onClick=showConfirm),
            antd.Button("With promise", onClick=showPromiseConfirm),
            antd.Button("Delete", onClick=showDeleteConfirm, type="dashed"),
            antd.Button("With extra props", onClick=showPropsConfirm, type="dashed"),
        ]
    )
