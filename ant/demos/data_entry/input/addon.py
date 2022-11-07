import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html

Option = antd.Select.Option
selectBefore = antd.Select(
    [Option("http://", value="http://"), Option("https://", value="https://")],
    defaultValue="http://",
    className="select-before",
)
selectAfter = antd.Select(
    [
        Option(".com", value=".com"),
        Option(".jp", value=".jp"),
        Option(".cn", value=".cn"),
        Option(".org", value=".org"),
    ],
    defaultValue=".com",
    className="select-after",
)


def app():
    return html.div(
        [
            html.div(
                antd.Input(
                    addonBefore="http://", addonAfter=".com", defaultValue="mysite"
                ),
                style=dict(marginBottom=16),
            ),
            html.div(
                antd.Input(
                    addonBefore=selectBefore,
                    addonAfter=selectAfter,
                    defaultValue="mysite",
                ),
                style=dict(marginBottom=16),
            ),
            html.div(
                antd.Input(
                    addonAfter=ant_icons.SettingOutlined([]), defaultValue="mysite"
                ),
                style=dict(marginBottom=16),
            ),
            html.div(
                antd.Input(addonBefore="http://", suffix=".com", defaultValue="mysite"),
                style=dict(marginBottom=16),
            ),
        ]
    )
