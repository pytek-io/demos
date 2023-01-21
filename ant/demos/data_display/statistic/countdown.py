import datetime

import reflect_antd as antd
import reflect_html as html

Countdown = antd.Statistic.Countdown
deadline = datetime.datetime.now() + datetime.timedelta(days=2, seconds=30)


def app():
    return antd.Row(
        [
            antd.Col(
                Countdown(
                    title="Countdown",
                    value=deadline,
                    onFinish=lambda: print("finished!"),
                ),
                span=12,
            ),
            antd.Col(
                Countdown(
                    title="Million Seconds", value=deadline, format="HH:mm:ss:SSS"
                ),
                span=12,
            ),
            antd.Col(
                Countdown(title="Day Level", value=deadline, format="D 天 H 时 m 分 s 秒"),
                span=24,
                style={"marginTop": 32},
            ),
        ],
        gutter=16,
    )
