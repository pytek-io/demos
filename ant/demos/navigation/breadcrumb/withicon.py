import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Breadcrumb(
        [
            antd.Breadcrumb.Item(ant_icons.HomeOutlined(), href=""),
            antd.Breadcrumb.Item(
                [ant_icons.UserOutlined(), html.span("Application List")], href=""
            ),
            antd.Breadcrumb.Item("Application"),
        ]
    )
