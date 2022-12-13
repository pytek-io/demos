import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            html.div(
                [
                    antd.Segmented(
                        size="large",
                        options=["Daily", "Weekly", "Monthly"],
                        style={"marginRight": 6},
                    ),
                    antd.Button("Button", type="primary", size="large"),
                ]
            ),
            html.div(
                [
                    antd.Segmented(
                        options=["Daily", "Weekly", "Monthly"],
                        style={"marginRight": 6},
                    ),
                    antd.Input(placeholder="default size", style={"width": 150}),
                ]
            ),
            html.div(
                [
                    antd.Segmented(
                        size="small",
                        options=["Daily", "Weekly", "Monthly"],
                        style={"marginRight": 6},
                    ),
                    antd.Select(
                        options=[{"value": "lucy", "title": "Lucy"}],
                        size="small",
                        defaultValue="lucy",
                        style={"width": 150},
                    ),
                ]
            ),
        ]
    )
