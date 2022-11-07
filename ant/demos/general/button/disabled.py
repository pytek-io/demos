import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Button("Primary", type="primary"),
            antd.Button("Primary(disabled)", type="primary", disabled=True),
            html.br(),
            antd.Button("Default"),
            antd.Button("Default(disabled)", disabled=True),
            html.br(),
            antd.Button("Dashed", type="dashed"),
            antd.Button("Dashed(disabled)", type="dashed", disabled=True),
            html.br(),
            antd.Button("Text", type="text"),
            antd.Button("Text(disabled)", type="text", disabled=True),
            html.br(),
            antd.Button("Link", type="link"),
            antd.Button("Link(disabled)", type="link", disabled=True),
            html.br(),
            antd.Button("Danger Default", danger=True),
            antd.Button("Danger Default(disabled)", danger=True, disabled=True),
            html.br(),
            antd.Button("Danger Text", danger=True, type="text"),
            antd.Button(
                "Danger Text(disabled)", danger=True, type="text", disabled=True
            ),
            html.br(),
            antd.Button("Danger Link", type="link", danger=True),
            antd.Button(
                "Danger Link(disabled)", type="link", danger=True, disabled=True
            ),
            html.div(
                [
                    antd.Button("Ghost", ghost=True),
                    antd.Button("Ghost(disabled)", ghost=True, disabled=True),
                ],
                className="site-button-ghost-wrapper",
            ),
        ]
    )
