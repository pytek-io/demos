import render_antd as antd
import render_html as html


def app(_):
    return antd.Row(
        [
            antd.Col("Col", xs={"span": 5, "offset": 1}, lg={"span": 6, "offset": 2}),
            antd.Col("Col", xs={"span": 11, "offset": 1}, lg={"span": 6, "offset": 2}),
            antd.Col("Col", xs={"span": 5, "offset": 1}, lg={"span": 6, "offset": 2}),
        ]
    )
