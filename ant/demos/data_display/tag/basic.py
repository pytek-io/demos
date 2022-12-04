import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    preventDefault = r.Callback(lambda: print("hi"), prevent_default=True)
    return html.div(
        [
            antd.Tag("Tag 1"),
            antd.Tag(
                html.a(
                    "Link", href="https://github.com/ant-design/ant-design/issues/1862"
                )
            ),
            antd.Tag("Tag 2", closable=True, onClose=lambda: print("closed")),
            antd.Tag("Prevent Default", closable=True, onClose=preventDefault),
        ]
    )
