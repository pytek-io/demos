import render_ant_icons as ant_icons
import render_antd as antd


def app():
    return antd.Timeline(
        items=[
            {"children": "Create a services site 2015-09-01"},
            {"children": "Solve initial network problems 2015-09-01"},
            {
                "children": "Technical testing 2015-09-01",
                "dot": ant_icons.ClockCircleOutlined(className="timeline-clock-icon"),
                "color": "red",
            },
            {"children": "Network problems being solved 2015-09-01"},
        ]
    )
