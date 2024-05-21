import render_antd as antd
import render_html as html


def app(_):
    return antd.Watermark(
        html.div("Ant Design", style={"height": 500}),
        content="Ant Design",
    )
