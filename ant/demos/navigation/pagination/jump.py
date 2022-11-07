from reflect_html import *
from reflect_antd import Pagination

from reflect import autorun


def onChange(pageNumber):
    print("Page: ", pageNumber)


def app():
    pagination1 = Pagination(showQuickJumper=True, defaultCurrent=2, total=500)
    autorun(lambda: print("Page: ", pagination1()))
    pagination2 = Pagination(
        showQuickJumper=True,
        defaultCurrent=2,
        total=500,
        disabled=True,
    )
    autorun(lambda: print("Page: ", pagination2()))
    return div([pagination1, br(), pagination2])
