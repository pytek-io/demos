import reflect_ant_icons as ant_icons
import reflect_antd as antd


def app():
    return antd.Timeline(
        items=[
            {"children": "Create a services site 2015-09-01"},
            {
                "children": "Solve initial network problems 2015-09-01",
                "color": "green",
            },
            {
                "children": "Technical testing 2015-09-01",
                "dot": ant_icons.ClockCircleOutlined(style={"fontSize": "16px"}),
            },
            {
                "children": "Network problems being solved 2015-09-01",
                "color": "red",
            },
            {
                "children": "Create a services site 2015-09-01",
            },
            {
                "dot": ant_icons.ClockCircleOutlined(style={"fontSize": "16px"}),
                "children": "Technical testing 2015-09-01",
            },
        ]
    )
