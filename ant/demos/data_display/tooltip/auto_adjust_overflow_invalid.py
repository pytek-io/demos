from reflect_html import *
from reflect_antd import Tooltip, Button
def app():
    return div([Tooltip(Button("Adjust automatically / 自动调整"), placement="left", title="Prompt Text", getPopupContainer=trigger => trigger.parentElement), br(), Tooltip(Button("Ignore / 不处理"), placement="left", title="Prompt Text", getPopupContainer=trigger => trigger.parentElement, autoAdjustOverflow=False)], style=wrapStyles)