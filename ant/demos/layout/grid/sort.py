import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Row(
        [
            antd.Col("col-18 col-push-6", span=18, push=6),
            antd.Col("col-6 col-pull-18", span=6, pull=18),
        ]
    )
