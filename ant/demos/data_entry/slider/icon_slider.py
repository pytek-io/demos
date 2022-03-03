from reflect_html import *
from reflect_antd import Slider
from reflect_ant_icons import FrownOutlined, SmileOutlined


def icon_slider(min_value, max_value):
    mid = int((max_value - min_value) / 2 + min_value)
    slider = Slider(min=min_value, max=max_value, defaultValue=mid)
    preColorCls = lambda: "" if slider() >= mid else "icon-wrapper-active"
    nextColorCls = lambda: "icon-wrapper-active" if slider() >= mid else ""
    return div(
        [
            FrownOutlined(className=preColorCls),
            slider,
            SmileOutlined(className=nextColorCls),
        ],
        className="icon-wrapper",
    )


def app():
    return icon_slider(min_value=0, max_value=20)
