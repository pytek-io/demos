import render_ant_icons as ant_icons
import render_html as html


def app(_):
    return html.div(
        [
            ant_icons.SmileTwoTone(),
            ant_icons.HeartTwoTone(twoToneColor="#eb2f96"),
            ant_icons.CheckCircleTwoTone(twoToneColor="#52c41a"),
        ],
        className="icons-list",
    )
