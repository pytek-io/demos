from render_antd import Button, Tooltip
from render_html import *


def app(_):
    return div([Tooltip(Button("Adjust automatically / 自动调整"), placement="left", title="Prompt Text", getPopupContainer=trigger => trigger.parentElement), br(), Tooltip(Button("Ignore / 不处理"), placement="left", title="Prompt Text", getPopupContainer=trigger => trigger.parentElement, autoAdjustOverflow=False)], style=wrapStyles)