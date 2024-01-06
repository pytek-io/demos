import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html

selectBefore = antd.Select(
    options=[
        {"label": "http://", "value": "http://"},
        {"label": "https://", "value": "https://"},
    ],
    defaultValue="http://",
    className="select-before",
)
selectAfter = antd.Select(
    options=[
        {"label": ".com", "value": ".com"},
        {"label": ".jp", "value": ".jp"},
        {"label": ".cn", "value": ".cn"},
        {"label": ".org", "value": ".org"},
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
                style={"marginBottom": 16},
            ),
            html.div(
                antd.Input(
                    addonBefore=selectBefore,
                    addonAfter=selectAfter,
                    defaultValue="mysite",
                ),
                style={"marginBottom": 16},
            ),
            html.div(
                antd.Input(
                    addonAfter=ant_icons.SettingOutlined([]), defaultValue="mysite"
                ),
                style={"marginBottom": 16},
            ),
            html.div(
                antd.Input(addonBefore="http://", suffix=".com", defaultValue="mysite"),
                style={"marginBottom": 16},
            ),
        ]
    )
