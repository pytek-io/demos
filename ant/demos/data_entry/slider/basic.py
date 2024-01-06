import render as r
import render_antd as antd
import render_html as html


def app():
    disable_switch = antd.Switch(size="small")
    slider1 = antd.Slider(defaultValue=30, disabled=disable_switch)
    slider2 = antd.Slider(range=True, defaultValue=[20, 50], disabled=disable_switch)
    r.autorun(lambda: print(slider1()))
    r.autorun(lambda: print(slider2()))
    return html.div([slider1, slider2, "Disabled: ", disable_switch])
