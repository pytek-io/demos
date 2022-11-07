import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Row(
        [
            antd.Col("Col", xs=dict(span=5, offset=1), lg=dict(span=6, offset=2)),
            antd.Col("Col", xs=dict(span=11, offset=1), lg=dict(span=6, offset=2)),
            antd.Col("Col", xs=dict(span=5, offset=1), lg=dict(span=6, offset=2)),
        ]
    )
