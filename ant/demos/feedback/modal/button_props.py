from reflect_html import *
from reflect_antd import Modal, Button
from reflect import create_observable


def app():
    is_modal_visible = create_observable(False)

    return div(
        [
            Button(
                "Open Modal with customized button props",
                type="primary",
                onClick=lambda: is_modal_visible.set(True),
            ),
            Modal(
                [p("Some contents..."), p("Some contents..."), p("Some contents...")],
                title="Basic Modal",
                visible=is_modal_visible,
                onOk=lambda: is_modal_visible.set(False),
                onCancel=lambda: is_modal_visible.set(False),
                okButtonProps=dict(disabled=True),
                cancelButtonProps=dict(disabled=True),
            ),
        ]
    )
