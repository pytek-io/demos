import render_ant_icons as ant_icons
import render_antd as antd


def app(_):
    return antd.Segmented(
        options=[
            {"label": "List", "icon": ant_icons.BarsOutlined(), "value": "List"},
            {
                "label": "Kanban",
                "icon": ant_icons.AppstoreOutlined(),
                "value": "Kanban",
            },
        ]
    )
