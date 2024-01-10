import render_antd as antd
import render_html as html


def app(_):
    return antd.Popover(
        antd.Button("Hover me", type="primary"),
        content=html.div([html.p("Content"), html.p("Content")]),
        title="Title",
    )
