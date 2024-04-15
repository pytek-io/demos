import render_antd as antd


def app(_):
    return antd.Breadcrumb(
        items=[
            {"title": "Home"},
            {"type": "separator", "separator": ":"},
            {"title": "Application Center", "href": ""},
            {"type": "separator"},
            {"title": "Application List", "href": ""},
            {"type": "separator"},
            {"title": "An Application"},
        ],
    )
