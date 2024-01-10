import render as r
import render_antd as antd
import render_html as html


def app(_):
    modal1Visible = r.ObservableValue(False)
    modal2Visible = r.ObservableValue(False)
    return html.div(
        [
            antd.Button(
                "Display a modal dialog at 20px to Top",
                type="primary",
                onClick=lambda: modal1Visible.set(True),
            ),
            antd.Modal(
                [
                    html.p("some contents..."),
                    html.p("some contents..."),
                    html.p("some contents..."),
                ],
                title="20px to Top",
                style={"top": 20},
                open=modal1Visible,
                onOk=lambda: modal1Visible.set(False),
                onCancel=lambda: modal1Visible.set(False),
            ),
            html.br(),
            html.br(),
            antd.Button(
                "Vertically centered modal dialog",
                type="primary",
                onClick=lambda: modal2Visible.set(True),
            ),
            antd.Modal(
                [
                    html.p("some contents..."),
                    html.p("some contents..."),
                    html.p("some contents..."),
                ],
                title="Vertically centered modal dialog",
                centered=True,
                open=modal2Visible,
                onOk=lambda: modal2Visible.set(False),
                onCancel=lambda: modal2Visible.set(False),
            ),
        ]
    )
