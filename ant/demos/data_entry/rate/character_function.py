import reflect as r
import reflect_antd as antd
import reflect_html as html

index_plus_one = r.js_arrow("index_plus_one", "({index}) => index + 1")

custom_icons = r.js_arrow(
    "custom_icons",
    """({ index }) => {
  icon = [
    reflect_ant_icons.FrownOutlined,
    reflect_ant_icons.FrownOutlined,
    reflect_ant_icons.MehOutlined,
    reflect_ant_icons.SmileOutlined,
    reflect_ant_icons.SmileOutlined,
  ][index];
  return icon();
};
""",
    ["reflect_ant_icons"],
)


def app():
    return html.div(
        [
            antd.Rate(defaultValue=2),
            html.br(),
            antd.Rate(defaultValue=2, character=index_plus_one),
            html.br(),
            antd.Rate(defaultValue=3, character=custom_icons),
        ]
    )
