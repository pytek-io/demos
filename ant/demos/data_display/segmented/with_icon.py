import reflect_antd as antd
import reflect_ant_icons as ant_icons


def app():
    return antd.Segmented(
        options=[
            {
                "label": "List",
                "icon": ant_icons.BarsOutlined(),
                "value": "List",
            },
            {
                "label": "Kanban",
                "icon": ant_icons.AppstoreOutlined(),
                "value": "Kanban",
            },
        ]
    )
