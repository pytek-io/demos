from reflect_html import *
from reflect_ant_icons import SmileTwoTone, HeartTwoTone, CheckCircleTwoTone


def app():
    return div(
        [
            SmileTwoTone(),
            HeartTwoTone(twoToneColor="#eb2f96"),
            CheckCircleTwoTone(twoToneColor="#52c41a"),
        ],
        className="icons-list",
    )
