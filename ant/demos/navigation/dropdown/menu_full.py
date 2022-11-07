import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

SubMenu = antd.Menu.SubMenu
menu = antd.Menu(
    [
        antd.Menu.ItemGroup(
            [
                antd.Menu.Item("Option 0", key="01"),
                antd.Menu.Item("Option 0", key="02"),
            ],
            key="group",
            title="Item Group",
        ),
        SubMenu(
            [
                antd.Menu.ItemGroup(
                    [
                        antd.Menu.Item("Option 1", key="1"),
                        antd.Menu.Item("Option 2", key="2"),
                    ],
                    key="g1",
                    title="Item 1",
                ),
                antd.Menu.ItemGroup(
                    [
                        antd.Menu.Item("Option 3", key="3"),
                        antd.Menu.Item("Option 4", key="4"),
                    ],
                    key="g2",
                    title="Item 2",
                ),
            ],
            key="sub1",
            icon=ant_icons.MailOutlined([]),
            title="Navigation One",
        ),
        SubMenu(
            [
                antd.Menu.Item("Option 5", key="5"),
                antd.Menu.Item("Option 6", key="6"),
                SubMenu(
                    [
                        antd.Menu.Item("Option 7", key="7"),
                        antd.Menu.Item("Option 8", key="8"),
                    ],
                    key="sub3",
                    title="Submenu",
                ),
            ],
            key="sub2",
            icon=ant_icons.AppstoreOutlined([]),
            title="Navigation Two",
        ),
        SubMenu(
            [
                antd.Menu.Item("Option 9", key="9"),
                antd.Menu.Item("Option 10", key="10"),
                antd.Menu.Item("Option 11", key="11"),
                antd.Menu.Item("Option 12", key="12"),
            ],
            key="sub4",
            icon=ant_icons.SettingOutlined([]),
            title="Navigation Three",
        ),
    ],
    selectedKeys=["1"],
    openKeys=["sub1"],
)


def app():
    return antd.Dropdown(
        html.a(
            ["Hover to check menu style", ant_icons.DownOutlined()],
            className="ant-dropdown-link",
            onClick=lambda e: e.preventDefault(),
        ),
        overlay=menu,
    )
