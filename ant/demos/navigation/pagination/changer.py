from reflect_html import *
from reflect_antd import Pagination
from reflect import Callback


def onShowSizeChange(current, pageSize):
    print(current, pageSize)


def app():
    return div(
        [
            Pagination(
                showSizeChanger=True,
                onShowSizeChange=Callback(onShowSizeChange),
                defaultCurrent=3,
                total=500,
            ),
            br(),
            Pagination(
                showSizeChanger=True,
                onShowSizeChange=Callback(onShowSizeChange),
                defaultCurrent=3,
                total=500,
                disabled=True,
            ),
        ]
    )
