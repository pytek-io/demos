import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

import reflect as r


def onClick(key):
    antd.message.info(f"Click on item {key[0]}")


def app():
    return antd.Dropdown(
        html.a(
            ["Hover me, Click menu item", ant_icons.DownOutlined()],
            className="ant-dropdown-link",
            onClick=lambda e: e.preventDefault(),
        ),
        menu={
            "items": [
                {"label": "1st menu item", "key": "1"},
                {"label": "2nd menu item", "key": "2"},
                {"label": "3rd menu item", "key": "3"},
            ],
            "onClick": r.Callback(onClick, args=("key",)),
        },
    )
