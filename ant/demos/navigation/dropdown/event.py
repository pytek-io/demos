import reflect as r
import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def onClick(key):
    antd.message.info(f"Click on item {key}")


def app():
    menu = antd.Menu(
        [
            antd.Menu.Item("1st menu item", key="1"),
            antd.Menu.Item("2nd menu item", key="2"),
            antd.Menu.Item("3rd menu item", key="3"),
        ],
        onClick=r.Callback(onClick, "key"),
    )
    return antd.Dropdown(
        html.a(
            ["Hover me, Click menu item", ant_icons.DownOutlined()],
            className="ant-dropdown-link",
            onClick=lambda e: e.preventDefault(),
        ),
        overlay=menu,
    )
