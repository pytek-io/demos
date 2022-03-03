from reflect_html import *
from reflect_antd import Button


def app():
    return div(
        [
            Button("Primary", type="primary", ghost=True),
            Button("Default", ghost=True),
            Button("Dashed", type="dashed", ghost=True),
        ],
        className="site-button-ghost-wrapper",
    )
