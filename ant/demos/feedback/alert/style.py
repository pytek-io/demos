from reflect_html import *
from reflect_antd import Alert


def app():
    return [
        Alert(message="Success Text", type="success"),
        Alert(message="Info Text", type="info"),
        Alert(message="Warning Text", type="warning"),
        Alert(message="Error Text", type="error"),
    ]
