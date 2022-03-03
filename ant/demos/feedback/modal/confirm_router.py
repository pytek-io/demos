from reflect_html import *
from reflect_antd import Modal, Button
from reflect_ant_icons import ExclamationCircleOutlined

confirm = Modal.confirm


def app():
    return Button("Confirm", onClick=showConfirm)
