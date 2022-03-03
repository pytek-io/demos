from reflect_html import *
from reflect_antd import Badge


def app():
    return a(Badge(span(className="head-example"), count=5), href="#")
