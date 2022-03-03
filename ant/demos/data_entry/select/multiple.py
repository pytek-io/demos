from reflect_html import *
from reflect_antd import Select
from reflect import js

from reflect import autorun

Option = Select.Option


def app():
    children = [
        Option(key, key=key)
        for key in (f"{chr(i + ord('a'))}{i}" for i in range(10, 36))
    ]
    select1 = Select(
        children,
        mode="multiple",
        allowClear=True,
        style=dict(width="100%"),
        placeholder="Please select",
        defaultValue=["a10", "c12"],
    )

    select2 = Select(
        children,
        mode="multiple",
        disabled=True,
        style=dict(width="100%"),
        placeholder="Please select",
        defaultValue=["a10", "c12"],
    )
    autorun(lambda: print(select1()))
    autorun(lambda: print(select2()))
    return select1, br(), select2
