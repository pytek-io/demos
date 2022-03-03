from reflect_html import *
from reflect_antd import Divider


def app():
    return [
        Divider(style=dict(borderWidth=2, borderColor="#7cb305")),
        Divider(style=dict(borderColor="#7cb305"), dashed=True),
        Divider("Text", style=dict(borderColor="#7cb305"), dashed=True),
        Divider(type="vertical", style=dict(height=60, borderColor="#7cb305")),
        Divider(
            type="vertical", style=dict(height=60, borderColor="#7cb305"), dashed=True
        ),
    ]
