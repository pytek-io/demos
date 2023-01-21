import reflect_ant_icons as ant_icons
import reflect_antd as antd


def app():
    return antd.Segmented(
        options=[
            {"icon": ant_icons.BarsOutlined(), "value": "List"},
            {"icon": ant_icons.AppstoreOutlined(), "value": "Kanban"},
        ]
    )
