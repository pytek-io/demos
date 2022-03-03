from reflect_html import *
from reflect_antd import Radio

from reflect import autorun


def app():
    radio_group = Radio.Group(
        [Radio("Option A", value="a"), Radio("Option B", value="b")], defaultValue="a"
    )
    autorun(lambda: print("selected", radio_group()))
    return radio_group
