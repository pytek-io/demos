import render_antd as antd
import render_html as html

Search = antd.Input.Search


def app(_):
    return html.div(
        [
            Search(placeholder="input search loading default", loading=True),
            html.br(),
            html.br(),
            Search(
                placeholder="input search loading with enterButton",
                loading=True,
                enterButton=True,
            ),
            html.br(),
            html.br(),
            Search(
                placeholder="input search text",
                enterButton="Search",
                size="large",
                loading=True,
            ),
        ]
    )
