import reflect as r
import reflect_antd as antd
import reflect_html as html
import reflect_ant_icons as ant_icons

index_plus_one = r.JSMethod("index_plus_one", "return index + 1;", "index")

custom_icons = r.JSMethod(
    "custom_icons",
    """
     const icon = [
      reflect_ant_icons.FrownOutlined,
      reflect_ant_icons.FrownOutlined,
      reflect_ant_icons.MehOutlined,
      reflect_ant_icons.SmileOutlined,
      reflect_ant_icons.SmileOutlined,
    ][arg.index];
     return createElement(icon);
""",
    "arg",
)


def app():
    return html.div(
        [
            ant_icons.CaretRightFilled(),
            # antd.Rate(defaultValue=2, character=index_plus_one),
            html.br(),
            antd.Rate(defaultValue=3, character=custom_icons),
        ]
    )
