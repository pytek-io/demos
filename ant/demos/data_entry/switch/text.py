from reflect_html import *
from reflect_antd import Switch
from reflect_ant_icons import CloseOutlined, CheckOutlined


def app():
    return div(
        [
            Switch(checkedChildren="开启", unCheckedChildren="关闭", defaultChecked=True),
            br(),
            Switch(checkedChildren="1", unCheckedChildren="0"),
            br(),
            Switch(
                checkedChildren=CheckOutlined([]),
                unCheckedChildren=CloseOutlined([]),
                defaultChecked=True,
            ),
        ]
    )
