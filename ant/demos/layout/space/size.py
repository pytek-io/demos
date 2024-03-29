import render_antd as antd
import render_html as html


def app(_):
    size = antd.Radio.Group(
        [
            antd.Radio("Small", value="small"),
            antd.Radio("Middle", value="middle"),
            antd.Radio("Large", value="large"),
        ],
        defaultValue="small",
    )
    return html.div(
        [
            size,
            html.br(),
            html.br(),
            antd.Space(
                [
                    antd.Button("Primary", type="primary"),
                    antd.Button("Default"),
                    antd.Button("Dashed", type="dashed"),
                    antd.Button("Link", type="link"),
                ],
                size=size,
            ),
        ]
    )
