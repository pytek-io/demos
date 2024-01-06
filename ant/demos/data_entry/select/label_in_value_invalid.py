from render_antd import Select
from render_html import *

from render import autorun



def app():
    raise Exception("not implemented")
    select = Select(
        [
            {"label": "Jack (100)", "value": "jack"},
            {"label": "Lucy (101)", "value": "lucy"},
        ],
        labelInValue=True,
        defaultValue=dict(value="lucy"),
        style=dict(width=120),
    )
    autorun(lambda: print(select()))
    return select
