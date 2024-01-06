import render_antd as antd
import render_html as html


def app():
    return antd.Breadcrumb(
        items=[
            {
                "title": "Home",
            },
            {
                "title": html.a("Application Center", href=""),
            },
            {
                "title": html.a("Application List", href=""),
            },
            {
                "title": "An Application",
            },
        ]
    )
