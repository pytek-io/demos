from reflect_html import *
from reflect_antd import Modal, Button
from reflect import make_observable


def app():
    is_modal_visible = make_observable(False)
    return [
        Button(
            "Open Modal of 1000px width",
            type="primary",
            onClick=lambda: is_modal_visible.set(True),
        ),
        Modal(
            [p("some contents..."), p("some contents..."), p("some contents...")],
            title="Modal 1000px width",
            centered=True,
            visible=is_modal_visible,
            onOk=lambda: is_modal_visible.set(False),
            onCancel=lambda: is_modal_visible.set(False),
            width=1000,
        ),
    ]
