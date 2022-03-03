from reflect_html import *
from reflect_antd import Alert


onClose = lambda: print("I have been closed.")


def app():
    return [
        Alert(
            message="Warning Text Warning Text Warning TextW arning Text Warning Text Warning TextWarning Text",
            type="warning",
            closable=True,
            onClose=onClose,
        ),
        Alert(
            message="Error Text",
            description="Error Description Error Description Error Description Error Description Error Description Error Description",
            type="error",
            closable=True,
            onClose=onClose,
        ),
    ]
