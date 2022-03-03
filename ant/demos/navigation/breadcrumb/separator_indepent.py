from reflect_html import *
from reflect_antd import Breadcrumb


def app():
    return Breadcrumb(
        [
            Breadcrumb.Item("Location"),
            Breadcrumb.Separator(":"),
            Breadcrumb.Item("Application Center", href=""),
            Breadcrumb.Separator(),
            Breadcrumb.Item("Application List", href=""),
            Breadcrumb.Separator(),
            Breadcrumb.Item("An Application"),
        ],
        separator="",
    )
