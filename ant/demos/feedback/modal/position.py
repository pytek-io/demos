from reflect_html import *
from reflect_antd import Modal, Button
from reflect import create_observable


def app():
    modal1Visible = create_observable(False)
    modal2Visible = create_observable(False)
    return [
        Button(
            "Display a modal dialog at 20px to Top",
            type="primary",
            onClick=lambda: modal1Visible.set(True),
        ),
        Modal(
            [p("some contents..."), p("some contents..."), p("some contents...")],
            title="20px to Top",
            style=dict(top=20),
            visible=modal1Visible,
            onOk=lambda: modal1Visible.set(False),
            onCancel=lambda: modal1Visible.set(False),
        ),
        br(),
        br(),
        Button(
            "Vertically centered modal dialog",
            type="primary",
            onClick=lambda: modal2Visible.set(True),
        ),
        Modal(
            [p("some contents..."), p("some contents..."), p("some contents...")],
            title="Vertically centered modal dialog",
            centered=True,
            visible=modal2Visible,
            onOk=lambda: modal2Visible.set(False),
            onCancel=lambda: modal2Visible.set(False),
        ),
    ]
