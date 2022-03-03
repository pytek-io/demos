from reflect_html import *
from reflect_antd import message, Button


def info():
    message.info("This is a normal message")


def app():
    return Button("Display normal message", type="primary", onClick=info)
