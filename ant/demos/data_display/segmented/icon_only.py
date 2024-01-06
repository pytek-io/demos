import render_ant_icons as ant_icons
import render_antd as antd


def app():
    return antd.Segmented(
        options=[
            {"icon": ant_icons.BarsOutlined(), "value": "List"},
            {"icon": ant_icons.AppstoreOutlined(), "value": "Kanban"},
        ]
    )
