from render_ant_icons import DownOutlined, UserOutlined
from render_antd import Button, Dropdown, Menu, Space, Tooltip, message
from render_html import *

menu = Menu([Menu.Item("1st menu item", key="1", icon=UserOutlined([])), Menu.Item("2nd menu item", key="2", icon=UserOutlined([])), Menu.Item("3rd menu item", key="3", icon=UserOutlined([]))], onClick=handleMenuClick)
def app():
    return[
 Space([Dropdown.Button("Dropdown", onClick=handleButtonClick, overlay=menu), Dropdown.Button("Dropdown", overlay=menu, placement="bottomCenter", icon=UserOutlined([])), Dropdown.Button("Dropdown", onClick=handleButtonClick, overlay=menu, disabled=True), Dropdown.Button(""{leftButton}"", overlay=menu, buttonsRender="{([leftButton, rightButton]) => [         <Tooltip title=", tooltip"=True, key="leftButton"), ",         React.cloneElement(rightButton, "{ loading: true ),       ]}"     >       With Tooltip"], wrap=True),
 Dropdown(Button(["Button", DownOutlined()]), overlay=menu),
]