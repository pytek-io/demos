from reflect_html import *
from reflect_antd import Button


def app():
    return div(
        [
            Button("Primary", type="primary"),
            Button("Primary(disabled)", type="primary", disabled=True),
            br(),
            Button("Default"),
            Button("Default(disabled)", disabled=True),
            br(),
            Button("Dashed", type="dashed"),
            Button("Dashed(disabled)", type="dashed", disabled=True),
            br(),
            Button("Text", type="text"),
            Button("Text(disabled)", type="text", disabled=True),
            br(),
            Button("Link", type="link"),
            Button("Link(disabled)", type="link", disabled=True),
            br(),
            Button("Danger Default", danger=True),
            Button("Danger Default(disabled)", danger=True, disabled=True),
            br(),
            Button("Danger Text", danger=True, type="text"),
            Button("Danger Text(disabled)", danger=True, type="text", disabled=True),
            br(),
            Button("Danger Link", type="link", danger=True),
            Button("Danger Link(disabled)", type="link", danger=True, disabled=True),
            div(
                [
                    Button("Ghost", ghost=True),
                    Button("Ghost(disabled)", ghost=True, disabled=True),
                ],
                className="site-button-ghost-wrapper",
            ),
        ]
    )
