from reflect_html import *
from reflect_antd import Card


def app():
    return [
        Card("More", title="Default size card", extra=a(href=True)),
        p("Card content"),
        p("Card content"),
        p("Card content"),
        Card("More", size="small", title="Small size card", extra=a(href=True)),
        p("Card content"),
        p("Card content"),
        p("Card content"),
    ]
        