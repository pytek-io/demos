from reflect_html import *
from reflect_antd import Descriptions


def app():
    return Descriptions(
        [
            Descriptions.Item("Zhou Maomao", label="UserName"),
            Descriptions.Item("1810000000", label="Telephone"),
            Descriptions.Item("Hangzhou, Zhejiang", label="Live"),
            Descriptions.Item(
                "No. 18, Wantang Road, Xihu District, Hangzhou, Zhejiang, China",
                label="Address",
                span=2,
            ),
            Descriptions.Item("empty", label="Remark"),
        ],
        title="User Info",
        layout="vertical",
    )
