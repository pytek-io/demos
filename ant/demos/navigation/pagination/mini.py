from reflect_html import *
from reflect_antd import Pagination


def showTotal():
    return f"Total {total} items"


def app():
    return [
        Pagination(size="small", total=50),
        Pagination(size="small", total=50, showSizeChanger=True, showQuickJumper=True),
        Pagination(size="small", total=50, 
        # showTotal=showTotal
        ),
        Pagination(
            size="small",
            total=50,
            disabled=True,
            # showTotal=showTotal,
            showSizeChanger=True,
            showQuickJumper=True,
        ),
    ]
