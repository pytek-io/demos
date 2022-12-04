import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Tooltip(
        html.span("Tooltip will show on mouse enter."), title="prompt text"
    )
