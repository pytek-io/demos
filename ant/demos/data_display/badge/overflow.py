from reflect_html import *
from reflect_antd import Badge, Space


def app():
    return Space(
        [
            Badge(a(href="#", className="head-example"), count=99),
            Badge(a(href="#", className="head-example"), count=100),
            Badge(a(href="#", className="head-example"), count=99, overflowCount=10),
            Badge(a(href="#", className="head-example"), count=1000, overflowCount=999),
        ],
        direction="vertical",
    )
