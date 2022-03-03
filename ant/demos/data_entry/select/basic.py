from reflect_html import *
from reflect_antd import Select

from reflect import autorun

Option = Select.Option


def app():
    select = Select(
        [
            Option("Jack", value="jack"),
            Option("Lucy", value="lucy"),
            Option("Disabled", value="disabled", disabled=True),
            Option("yiminghe", value="Yiminghe"),
        ],
        defaultValue="lucy",
        style=dict(width=120),
    )
    autorun(lambda: print("selected", select()))
    return div(
        [
            select,
            Select(
                Option("Lucy", value="lucy"),
                defaultValue="lucy",
                style=dict(width=120),
                disabled=True,
            ),
            Select(
                Option("Lucy", value="lucy"),
                defaultValue="lucy",
                style=dict(width=120),
                loading=True,
            ),
            Select(
                Option("Lucy", value="lucy"),
                defaultValue="lucy",
                style=dict(width=120),
                allowClear=True,
            ),
        ]
    )
