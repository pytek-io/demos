from reflect_html import *
from reflect_antd import Modal, Button


def app():
    return Button("Open modal to close in 5s", onClick=countDown)
