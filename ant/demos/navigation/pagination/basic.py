from reflect_html import *
from reflect_antd import Pagination

def app():
    return [Pagination(defaultCurrent=1, total=50)]
