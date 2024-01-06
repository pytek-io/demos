from render_html import *
from render_antd import Modal, Button
from render_ant_icons import ExclamationCircleOutlined

confirm = Modal.confirm


def app():
    return Button("Confirm", onClick=showConfirm)
