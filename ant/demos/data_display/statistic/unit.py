from reflect_html import *
from reflect_antd import Statistic, Row, Col
from reflect_ant_icons import LikeOutlined


def app():
    return Row(
        [
            Col(
                Statistic(title="Feedback", value=1128, prefix=LikeOutlined([])),
                span=12,
            ),
            Col(Statistic(title="Unmerged", value=93, suffix="/ 100"), span=12),
        ],
        gutter=16,
    )
