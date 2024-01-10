import render as r
import render_antd as antd
import render_html as html


def app(_):
    is_modal_visible = r.ObservableValue(False)
    return html.div(
        [
            antd.Button(
                "Open Modal of 1000px width",
                type="primary",
                onClick=lambda: is_modal_visible.set(True),
            ),
            antd.Modal(
                [
                    html.p("some contents..."),
                    html.p("some contents..."),
                    html.p("some contents..."),
                ],
                title="Modal 1000px width",
                centered=True,
                open=is_modal_visible,
                onOk=lambda: is_modal_visible.set(False),
                onCancel=lambda: is_modal_visible.set(False),
                width=1000,
            ),
        ]
    )
