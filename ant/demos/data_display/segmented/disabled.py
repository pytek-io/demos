import render_antd as antd
import render_html as html


def app(_):
    return html.div(
        [
            antd.Segmented(defaultValue="Map", options=["Map", "Transit", "Satellite"]),
            html.br(),
            antd.Segmented(
                options=[
                    "Daily",
                    {"label": "Weekly", "value": "Weekly", "disabled": True},
                    "Monthly",
                    {"label": "Quarterly", "value": "Quarterly", "disabled": True},
                    "Yearly",
                ]
            ),
        ]
    )
