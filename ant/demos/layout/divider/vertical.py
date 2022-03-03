from reflect_html import *
from reflect_antd import Divider


def app():
    return [
        Divider(type="vertical"),
        a("Link", href="#"),
        Divider(type="vertical"),
        a("Link", href="#"),
    ]
