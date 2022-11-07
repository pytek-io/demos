import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

SubMenu = antd.Menu.SubMenu
menu = antd.Menu(
    [
        antd.Menu.ItemGroup(
            [antd.Menu.Item("1st menu item"), antd.Menu.Item("2nd menu item")],
            title="Group title",
        ),
        SubMenu(
            [antd.Menu.Item("3rd menu item"), antd.Menu.Item("4th menu item")],
            title="sub menu",
        ),
        SubMenu(
            [antd.Menu.Item("5d menu item"), antd.Menu.Item("6th menu item")],
            title="disabled sub menu",
            disabled=True,
        ),
    ]
)


def app():
    return antd.Dropdown(
        html.a(
            ["Cascading menu", ant_icons.DownOutlined()],
            className="ant-dropdown-link",
            onClick=lambda e: e.preventDefault(),
        ),
        overlay=menu,
    )
