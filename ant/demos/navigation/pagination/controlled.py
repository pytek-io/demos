from reflect_html import *
from reflect_antd import Pagination

from reflect import autorun


def app():
    pagination = Pagination(defaultCurrent=3, total=50)
    autorun(lambda: print(pagination()))
    return pagination
