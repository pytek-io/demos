from reflect_html import *
from reflect_antd import Select
from reflect_ant_icons import SmileOutlined, MehOutlined

from reflect import autorun

Option = Select.Option


def app():
    smileIcon = SmileOutlined()
    mehIcon = MehOutlined()
    select = Select(
        [
            Option("Jack", value="jack"),
            Option("Lucy", value="lucy"),
            Option("Disabled", value="disabled", disabled=True),
            Option("yiminghe", value="Yiminghe"),
        ],
        suffixIcon=smileIcon,
        defaultValue="lucy",
        style=dict(width=120),
    )
    autorun(lambda: print("selected", select()))
    return div(
        [
            select,
            Select(
                Option("Lucy", value="lucy"),
                suffixIcon=mehIcon,
                defaultValue="lucy",
                style=dict(width=120),
                disabled=True,
            ),
        ]
    )
