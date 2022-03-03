from reflect_html import *
from reflect_antd import Alert
from reflect import Component

ErrorBoundary = Alert.ErrorBoundary


class ThrowError(Component):
    pass


def app():
    return ThrowError()
