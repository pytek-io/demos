from reflect_html import *
from reflect_antd import Badge


def app():
    return [
        Badge(a(href="#", className="head-example"), size="default", count=5),
        Badge(a(href="#", className="head-example"), size="small", count=5),
    ]
