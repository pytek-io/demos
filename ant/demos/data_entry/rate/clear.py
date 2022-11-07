from reflect_html import *
from reflect_antd import Rate


def app():
    return div(
        [
            Rate(defaultValue=3),
            span("allowClear: true", className="ant-rate-text"),
            br(),
            Rate(allowClear=False, defaultValue=3),
            span("allowClear: false", className="ant-rate-text"),
        ]
    )
