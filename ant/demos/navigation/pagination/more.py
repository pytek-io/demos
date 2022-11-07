from reflect_html import *
from reflect_antd import Pagination


def app():
    return div([Pagination(defaultCurrent=6, total=500)])
