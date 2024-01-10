import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def icon_slider(min_value, max_value):
    mid = int((max_value - min_value) / 2 + min_value)
    slider = antd.Slider(min=min_value, max=max_value, defaultValue=mid)
    preColorCls = lambda: "" if slider() >= mid else "icon-wrapper-active"
    nextColorCls = lambda: "icon-wrapper-active" if slider() >= mid else ""
    return html.div(
        [
            ant_icons.FrownOutlined(className=preColorCls),
            slider,
            ant_icons.SmileOutlined(className=nextColorCls),
        ],
        className="icon-wrapper",
    )


def app(_):
    return icon_slider(min_value=0, max_value=20)
