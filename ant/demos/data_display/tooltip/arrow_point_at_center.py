import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Tooltip(
                antd.Button("Align edge / 边缘对齐"),
                placement="topLeft",
                title="Prompt Text",
            ),
            antd.Tooltip(
                antd.Button("Arrow points to center / 箭头指向中心"),
                placement="topLeft",
                title="Prompt Text",
                arrow={"pointAtCenter": True},
            ),
        ]
    )
