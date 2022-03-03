from reflect_html import *
from reflect_antd import Statistic, Row, Col

from datetime import datetime, timedelta

Countdown = Statistic.Countdown

deadline = datetime.now() + timedelta(days=2, seconds=30)


def app():

    return Row(
        [
            Col(
                Countdown(
                    title="Countdown",
                    value=deadline,
                    onFinish=lambda: print("finished!"),
                ),
                span=12,
            ),
            Col(
                Countdown(
                    title="Million Seconds", value=deadline, format="HH:mm:ss:SSS"
                ),
                span=12,
            ),
            Col(
                Countdown(title="Day Level", value=deadline, format="D 天 H 时 m 分 s 秒"),
                span=24,
                style=dict(marginTop=32),
            ),
        ],
        gutter=16,
    )
