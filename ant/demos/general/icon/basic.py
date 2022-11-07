import reflect_ant_icons as ant_icons
import reflect_html as html


def app():
    return html.div(
        [
            ant_icons.HomeOutlined(),
            ant_icons.SettingFilled(),
            ant_icons.SmileOutlined(),
            ant_icons.SyncOutlined(spin=True),
            ant_icons.SmileOutlined(rotate=180),
            ant_icons.LoadingOutlined(),
        ],
        className="icons-list",
    )
