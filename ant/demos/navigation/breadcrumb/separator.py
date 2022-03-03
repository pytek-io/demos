from reflect_html import *
from reflect_antd import Breadcrumb


def app():
    return Breadcrumb(
        [
            Breadcrumb.Item("Home"),
            Breadcrumb.Item("Application Center", href=""),
            Breadcrumb.Item("Application List", href=""),
            Breadcrumb.Item("An Application"),
        ],
        separator=">",
    )
