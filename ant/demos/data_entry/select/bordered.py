from reflect_html import *
from reflect_antd import Select

Option = Select.Option


def app():
    return [
        Select(
            [
                Option("Jack", value="jack"),
                Option("Lucy", value="lucy"),
                Option("yiminghe", value="Yiminghe"),
            ],
            defaultValue="lucy",
            style=dict(width=120),
            bordered=False,
        ),
        Select(
            Option("Lucy", value="lucy"),
            defaultValue="lucy",
            style=dict(width=120),
            disabled=True,
            bordered=False,
        ),
    ]
