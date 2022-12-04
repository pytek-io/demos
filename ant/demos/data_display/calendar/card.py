import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        antd.Calendar(fullscreen=False, onPanelChange=r.Callback(print)),
        className="site-calendar-demo-card",
    )
