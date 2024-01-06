import render_antd as antd
import render_html as html


def app():
    return html.div(
        [
            antd.Divider("Percentage columns", orientation="left"),
            antd.Row([antd.Col("2 / 5", flex=2), antd.Col("3 / 5", flex=3)]),
            antd.Divider("Fill rest", orientation="left"),
            antd.Row(
                [antd.Col("100px", flex="100px"), antd.Col("Fill Rest", flex="auto")]
            ),
            antd.Divider("Raw flex style", orientation="left"),
            antd.Row(
                [
                    antd.Col("1 1 200px", flex="1 1 200px"),
                    antd.Col("0 1 300px", flex="0 1 300px"),
                ]
            ),
            antd.Row(
                [
                    antd.Col(
                        html.div("none", style={"padding": "0 16px"}), flex="none"
                    ),
                    antd.Col("auto with no-wrap", flex="auto"),
                ],
                wrap=False,
            ),
        ]
    )
