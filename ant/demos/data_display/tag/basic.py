import render as r
import render_antd as antd
import render_html as html


def app(_):
    preventDefault = r.Callback(lambda: print("hi"), prevent_default=True)
    return html.div(
        [
            antd.Tag("Tag 1"),
            antd.Tag(
                html.a(
                    "Link", href="https://github.com/ant-design/ant-design/issues/1862"
                )
            ),
            antd.Tag("Tag 2", closeIcon=True, onClose=lambda: print("closed")),
            antd.Tag("Prevent Default", closeIcon=True, onClose=preventDefault),
        ]
    )
