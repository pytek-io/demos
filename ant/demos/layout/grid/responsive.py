import render_antd as antd
import render_html as html


def app(_):
    return antd.Row(
        [
            antd.Col("Col", xs=2, sm=4, md=6, lg=8, xl=10),
            antd.Col("Col", xs=20, sm=16, md=12, lg=8, xl=4),
            antd.Col("Col", xs=2, sm=4, md=6, lg=8, xl=10),
        ]
    )
