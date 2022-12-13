import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [
            antd.Segmented(
                options=["Daily", "Weekly", "Monthly", "Quarterly", "Yearly"],
                size="large",
            ),
            html.br(),
            antd.Segmented(
                options=["Daily", "Weekly", "Monthly", "Quarterly", "Yearly"],
            ),
            html.br(),
            antd.Segmented(
                options=["Daily", "Weekly", "Monthly", "Quarterly", "Yearly"],
                size="small",
            ),
        ]
    )
