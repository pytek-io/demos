from reflect_html import *
from reflect_antd import Pagination
from reflect import Callback


def itemRender(*args):
    print(args)
    current, type_, originalElement
    if type_ == "prev":
        return a("Previous")
    if type_ == "next":
        return a("Next")
    return originalElement


def app():
    raise NotImplementedError()
    return Pagination(
        total=500,
        # itemRender=Callback(itemRender),
    )
