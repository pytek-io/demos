import render as r
import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def onClick(key):
    print(f"Click on item {key}")


def app(_):
    return antd.Dropdown(
        html.a(
            antd.Space(
                [html.div(["Hover me, Click menu item"]), ant_icons.DownOutlined()]
            ),
            className="ant-dropdown-link",
            onClick=r.Callback(prevent_default=True),
        ),
        menu={
            "items": [
                {"label": "1st menu item", "key": "1"},
                {"label": "2nd menu item", "key": "2"},
                {"label": "3rd menu item", "key": "3"},
            ],
            "onClick": r.Callback(onClick, data_paths=[[0, "key"]]),
        },
    )
