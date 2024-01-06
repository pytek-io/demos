from render_html import *
from render_antd import Alert
from render import Component

ErrorBoundary = Alert.ErrorBoundary


class ThrowError(Component):
    pass


def app():
    return ThrowError()
