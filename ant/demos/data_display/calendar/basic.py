from reflect_html import *
from reflect_antd import Calendar
from reflect import Callback

def app():
    return Calendar(
        onPanelChange=Callback(print))
