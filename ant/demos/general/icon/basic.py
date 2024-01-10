import render_ant_icons as ant_icons
import render_html as html


def app(_):
    return html.div(
        [
            ant_icons.HomeOutlined(),
            ant_icons.SettingFilled(),
            ant_icons.SmileOutlined(),
            ant_icons.SyncOutlined(spin=True),
            ant_icons.LoadingOutlined(),
        ],
        className="icons-list",
    )
