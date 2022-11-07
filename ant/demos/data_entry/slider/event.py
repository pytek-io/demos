import reflect as r
import reflect_antd as antd
import reflect_html as html


def onAfterChange(value):
    print("onAfterChange", value)


def app():
    slider1 = antd.Slider(defaultValue=30, onAfterChange=r.Callback(onAfterChange))
    r.autorun(lambda: print("onChange", slider1()))
    slider2 = antd.Slider(
        range=True,
        step=10,
        defaultValue=[20, 50],
        onAfterChange=r.Callback(onAfterChange),
    )
    r.autorun(lambda: print("onChange", slider2()))
    return html.div([slider1, slider2])
