import reflect_antd as antd
import reflect_html as html

style = {"background": "#0092ff", "padding": "8px 0"}


def app():
    return html.div(
        [
            antd.Divider("Horizontal", orientation="left"),
            antd.Row(
                [
                    antd.Col(
                        html.div("col-6", style=style), className="gutter-row", span=6
                    ),
                    antd.Col(
                        html.div("col-6", style=style), className="gutter-row", span=6
                    ),
                    antd.Col(
                        html.div("col-6", style=style), className="gutter-row", span=6
                    ),
                    antd.Col(
                        html.div("col-6", style=style), className="gutter-row", span=6
                    ),
                ],
                gutter=16,
            ),
            antd.Divider("Responsive", orientation="left"),
            antd.Row(
                [
                    antd.Col(
                        html.div("col-6", style=style), className="gutter-row", span=6
                    ),
                    antd.Col(
                        html.div("col-6", style=style), className="gutter-row", span=6
                    ),
                    antd.Col(
                        html.div("col-6", style=style), className="gutter-row", span=6
                    ),
                    antd.Col(
                        html.div("col-6", style=style), className="gutter-row", span=6
                    ),
                ],
                gutter={"xs": 8, "sm": 16, "md": 24, "lg": 32},
            ),
            antd.Divider("Vertical", orientation="left"),
            antd.Row(
                [
                    antd.Col(
                        html.div("col-6", style=style), className="gutter-row", span=6
                    ),
                    antd.Col(
                        html.div("col-6", style=style), className="gutter-row", span=6
                    ),
                    antd.Col(
                        html.div("col-6", style=style), className="gutter-row", span=6
                    ),
                    antd.Col(
                        html.div("col-6", style=style), className="gutter-row", span=6
                    ),
                    antd.Col(
                        html.div("col-6", style=style), className="gutter-row", span=6
                    ),
                    antd.Col(
                        html.div("col-6", style=style), className="gutter-row", span=6
                    ),
                    antd.Col(
                        html.div("col-6", style=style), className="gutter-row", span=6
                    ),
                    antd.Col(
                        html.div("col-6", style=style), className="gutter-row", span=6
                    ),
                ],
                gutter=[16, 24],
            ),
        ]
    )
