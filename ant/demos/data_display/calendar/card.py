from reflect_html import *
from reflect_antd import Calendar
from reflect import Callback


def app():
    return div(
        Calendar(fullscreen=False, onPanelChange=Callback(print)),
        className="site-calendar-demo-card",
    )
