import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    is_modal_visible = r.create_observable(False)
    return html.div(
        [
            antd.Button(
                "Open Modal with customized button props",
                type="primary",
                onClick=lambda: is_modal_visible.set(True),
            ),
            antd.Modal(
                [
                    html.p("Some contents..."),
                    html.p("Some contents..."),
                    html.p("Some contents..."),
                ],
                title="Basic Modal",
                visible=is_modal_visible,
                onOk=lambda: is_modal_visible.set(False),
                onCancel=lambda: is_modal_visible.set(False),
                okButtonProps=dict(disabled=True),
                cancelButtonProps=dict(disabled=True),
            ),
        ]
    )
