from reflect_html import *
from reflect_antd import Tooltip


def app():
    return Tooltip(span("Tooltip will show on mouse enter."), title="prompt text")
