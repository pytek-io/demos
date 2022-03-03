from reflect_html import *
from reflect_antd import Select

from reflect import autorun

Option, OptGroup = Select.Option, Select.OptGroup


def app():
    select = Select(
        [
            OptGroup(
                [Option("Jack", value="jack"), Option("Lucy", value="lucy")],
                label="Manager",
            ),
            OptGroup(Option("yiminghe", value="Yiminghe"), label="Engineer"),
        ],
        defaultValue="lucy",
        style=dict(width=200),
    )
    autorun(lambda: print(select()))
    return select