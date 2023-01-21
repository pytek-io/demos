import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Tooltip(
        html.span("Tooltip will destroy when hidden."),
        destroyTooltipOnHide={"keepParent": False},
        title="prompt text",
    )
