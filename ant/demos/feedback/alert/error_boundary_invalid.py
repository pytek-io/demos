from render import Component
from render_antd import Alert
from render_html import *

ErrorBoundary = Alert.ErrorBoundary


class ThrowError(Component):
    pass


def app(_):
    return ThrowError()
