from render_antd import Card
from render_html import *


def app():
    return[
 Card([Card("More", type="inner", title="Inner Card title", extra="{a(href=", #"=True), "}">       Inner Card content"], title="Card title"),
 Card("More", style=dict(marginTop=16), type="inner", title="Inner Card title", extra="{<a href=", #"=True),
]