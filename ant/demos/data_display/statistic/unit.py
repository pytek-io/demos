import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


def app():
    return antd.Row(
        [
            antd.Col(
                antd.Statistic(
                    title="Feedback", value=1128, prefix=ant_icons.LikeOutlined([])
                ),
                span=12,
            ),
            antd.Col(
                antd.Statistic(title="Unmerged", value=93, suffix="/ 100"), span=12
            ),
        ],
        gutter=16,
    )
