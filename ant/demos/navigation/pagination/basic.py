from reflect_html import *
from reflect_antd import Pagination

def app():
    return div([Pagination(defaultCurrent=1, total=50)])
