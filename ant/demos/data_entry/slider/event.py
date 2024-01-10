import render as r
import render_antd as antd
import render_html as html


def onAfterChange(value):
    print("onAfterChange", value)


def app(_):
    slider1 = antd.Slider(defaultValue=30, onAfterChange=onAfterChange)
    r.autorun(lambda: print("slider1", slider1()))
    slider2 = antd.Slider(
        range=True, step=10, defaultValue=[20, 50], onAfterChange=onAfterChange
    )
    r.autorun(lambda: print("slider2", slider2()))
    return html.div([slider1, slider2])
