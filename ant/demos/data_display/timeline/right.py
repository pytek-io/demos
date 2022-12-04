import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Timeline(
        [
            antd.Timeline.Item("Create a services site 2015-09-01"),
            antd.Timeline.Item("Solve initial network problems 2015-09-01"),
            antd.Timeline.Item(
                "Technical testing 2015-09-01",
                dot=ant_icons.ClockCircleOutlined(
                    style=dict(fontSize="16px", color="red")
                ),
            ),
            antd.Timeline.Item("Network problems being solved 2015-09-01"),
        ],
        mode="right",
    )
