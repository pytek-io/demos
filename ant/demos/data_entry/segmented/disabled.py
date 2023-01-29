import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Segmented(options=["Map", "Transit", "Satellite"], disabled=True),
            antd.Segmented(
                options=[
                    "Daily",
                    {"label": "Weekly", "value": "Weekly", "disabled": True},
                    "Monthly",
                    {"label": "Quarterly", "value": "Quarterly", "disabled": True},
                    "Yearly",
                ],
                disabled=True,
            ),
        ]
    )
