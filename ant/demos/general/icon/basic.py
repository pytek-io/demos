from reflect_html import *
from reflect_ant_icons import HomeOutlined, SettingFilled, SmileOutlined, SyncOutlined, LoadingOutlined

def app():
    return div(
        [
            HomeOutlined(),
            SettingFilled(),
            SmileOutlined(),
            SyncOutlined(spin=True),
            SmileOutlined(rotate=180),
            LoadingOutlined(),
        ],
        className="icons-list",
    )
