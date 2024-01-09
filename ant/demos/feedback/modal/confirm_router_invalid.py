from render_ant_icons import ExclamationCircleOutlined
from render_antd import Button, Modal
from render_html import *

confirm = Modal.confirm


def app():
    return Button("Confirm", onClick=showConfirm)
