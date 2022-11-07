import reflect as r
import reflect_antd as antd
import reflect_html as html

routes = [
    {"path": "index", "breadcrumbName": "First-level Menu"},
    {"path": "first", "breadcrumbName": "Second-level Menu"},
    {"path": "second", "breadcrumbName": "Third-level Menu"},
]


def app():
    return antd.PageHeader(
        className="site-page-header",
        title="Title",
        breadcrumb=routes,
        subTitle="This is a subtitle",
    )
