import render as r
import render_antd as antd
import render_html as html

index_plus_one = r.js_arrow("index_plus_one", "({index}) => index + 1")

custom_icons = r.js_arrow(
    "custom_icons",
    """({ index }) => {
  return [
    render_ant_icons.FrownOutlined,
    render_ant_icons.FrownOutlined,
    render_ant_icons.MehOutlined,
    render_ant_icons.SmileOutlined,
    render_ant_icons.SmileOutlined,
  ][index]();
};
""",
    ["render_ant_icons"],
)


def app(_):
    return html.div(
        [
            antd.Rate(defaultValue=2),
            html.br(),
            antd.Rate(defaultValue=2, character=index_plus_one),
            html.br(),
            antd.Rate(defaultValue=3, character=custom_icons),
        ]
    )
