from reflect_html import *
from reflect_antd import Badge


def app():
    return Badge(a(href="#", className="head-example"), count=5, offset=[10, 10])
