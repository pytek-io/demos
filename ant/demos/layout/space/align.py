import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            html.div(
                antd.Space(
                    [
                        "center",
                        antd.Button("Primary", type="primary"),
                        html.span("Block", className="mock-block"),
                    ],
                    align="center",
                ),
                className="space-align-block",
            ),
            html.div(
                antd.Space(
                    [
                        "start",
                        antd.Button("Primary", type="primary"),
                        html.span("Block", className="mock-block"),
                    ],
                    align="start",
                ),
                className="space-align-block",
            ),
            html.div(
                antd.Space(
                    [
                        "end",
                        antd.Button("Primary", type="primary"),
                        html.span("Block", className="mock-block"),
                    ],
                    align="end",
                ),
                className="space-align-block",
            ),
            html.div(
                antd.Space(
                    [
                        "baseline",
                        antd.Button("Primary", type="primary"),
                        html.span("Block", className="mock-block"),
                    ],
                    align="baseline",
                ),
                className="space-align-block",
            ),
        ],
        className="space-align-container",
    )
