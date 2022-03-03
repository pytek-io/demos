from reflect import js
from reflect_html import *
from reflect_antd import PageHeader

routes = [
    {
        "path": "index",
        "breadcrumbName": "First-level Menu",
    },
    {
        "path": "first",
        "breadcrumbName": "Second-level Menu",
    },
    {
        "path": "second",
        "breadcrumbName": "Third-level Menu",
    },
]


def app():
    return PageHeader(
        className="site-page-header",
        title="Title",
        breadcrumb=routes,
        subTitle="This is a subtitle",
    )
