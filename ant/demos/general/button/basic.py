from reflect_html import div, br
from reflect_antd import Button


def app():
    return div([
        Button("Primary Button", type="primary"),
        Button("Default Button"),
        Button("Dashed Button", type="dashed"),
        br(),
        Button("Text Button", type="text"),
        Button("Link Button", type="link"),
    ])
