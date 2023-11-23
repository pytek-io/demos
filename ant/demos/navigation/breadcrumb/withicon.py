import reflect_ant_icons as ant_icons
import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Breadcrumb(
        items=[
            {"title": ant_icons.HomeOutlined(), "href": ""},
            {
                "title": [ant_icons.UserOutlined(), html.span("Application List")],
                "href": "",
            },
            {"title": "Application"},
        ]
    )
