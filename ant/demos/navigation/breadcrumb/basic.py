from reflect_html import *
from reflect_antd import Breadcrumb


def app():
    return Breadcrumb(
        [
            Breadcrumb.Item("Home"),
            Breadcrumb.Item(a("Application Center", href="")),
            Breadcrumb.Item(a("Application List", href="")),
            Breadcrumb.Item("An Application"),
        ]
    )
