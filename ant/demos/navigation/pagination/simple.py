from reflect_html import *
from reflect_antd import Pagination


def app():
    return div([
        Pagination(simple=True, defaultCurrent=2, total=50),
        br(),
        Pagination(disabled=True, simple=True, defaultCurrent=2, total=50),
    ])
