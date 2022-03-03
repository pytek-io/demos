from reflect_html import *
from reflect_antd import Radio


def app():
    return (
        Radio.Group(
            [
                Radio("A", value=1),
                Radio("B", value=2),
                Radio("C", value=3),
                Radio("D", value=4),
            ],
            name="radiogroup",
            defaultValue=1,
        ),
    )
