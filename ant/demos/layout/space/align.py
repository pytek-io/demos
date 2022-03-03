from reflect_html import *
from reflect_antd import Space, Button


def app():
    return div(
        [
            div(
                Space(
                    [
                        "center",
                        Button("Primary", type="primary"),
                        span("Block", className="mock-block"),
                    ],
                    align="center",
                ),
                className="space-align-block",
            ),
            div(
                Space(
                    [
                        "start",
                        Button("Primary", type="primary"),
                        span("Block", className="mock-block"),
                    ],
                    align="start",
                ),
                className="space-align-block",
            ),
            div(
                Space(
                    [
                        "end",
                        Button("Primary", type="primary"),
                        span("Block", className="mock-block"),
                    ],
                    align="end",
                ),
                className="space-align-block",
            ),
            div(
                Space(
                    [
                        "baseline",
                        Button("Primary", type="primary"),
                        span("Block", className="mock-block"),
                    ],
                    align="baseline",
                ),
                className="space-align-block",
            ),
        ],
        className="space-align-container",
    )
