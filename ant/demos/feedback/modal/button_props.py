import render as r
import render_antd as antd
import render_html as html


def app():
    is_modal_visible = r.ObservableValue(False)
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
                open=is_modal_visible,
                onOk=lambda: is_modal_visible.set(False),
                onCancel=lambda: is_modal_visible.set(False),
                okButtonProps={"disabled": True},
                cancelButtonProps={"disabled": True},
            ),
        ]
    )
