import reflect as r
import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Menu(
        [
            antd.Menu.SubMenu(
                [
                    antd.Menu.ItemGroup(
                        [
                            antd.Menu.Item("Option 1", key="1"),
                            antd.Menu.Item("Option 2", key="2"),
                        ],
                        title="Item 1",
                    ),
                    antd.Menu.ItemGroup(
                        [
                            antd.Menu.Item("Option 3", key="3"),
                            antd.Menu.Item("Option 4", key="4"),
                        ],
                        title="Item 2",
                    ),
                ],
                key="sub1",
                icon=ant_icons.MailOutlined(),
                title="Navigation One",
            ),
            antd.Menu.SubMenu(
                [
                    antd.Menu.Item("Option 5", key="5"),
                    antd.Menu.Item("Option 6", key="6"),
                    antd.Menu.SubMenu(
                        [
                            antd.Menu.Item("Option 7", key="7"),
                            antd.Menu.Item("Option 8", key="8"),
                        ],
                        key="sub3",
                        title="Submenu",
                    ),
                ],
                key="sub2",
                icon=ant_icons.AppstoreOutlined(),
                title="Navigation Two",
            ),
            antd.Menu.SubMenu(
                [
                    antd.Menu.Item("Option 9", key="9"),
                    antd.Menu.Item("Option 10", key="10"),
                    antd.Menu.Item("Option 11", key="11"),
                    antd.Menu.Item("Option 12", key="12"),
                ],
                key="sub4",
                icon=ant_icons.SettingOutlined(),
                title="Navigation Three",
            ),
        ],
        onClick=r.Callback(lambda key: print(f"clicked {key}"), args="key"),
        style=dict(width=256),
        mode="vertical",
    )
