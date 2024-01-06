import render_ant_icons as ant_icons
import render_antd as antd
import render_html as html


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
