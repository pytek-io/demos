from reflect_html import *
from reflect_antd import Radio

from reflect import autorun


def app():

    result = Radio.Group(
        [
            Radio("A", value=1),
            Radio("B", value=2),
            Radio("C", value=3),
            Radio("D", value=4),
        ],
        defaultValue=1,
    )
    autorun(lambda: print("radio checked", result()))
    return result