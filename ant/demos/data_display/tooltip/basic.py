import render_antd as antd
import render_html as html


def app(_):
    return antd.Tooltip(
        html.span("Tooltip will show on mouse enter."), title="prompt text"
    )
