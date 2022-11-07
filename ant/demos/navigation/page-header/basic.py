from reflect_html import *
from reflect_antd import PageHeader


def app():
    return PageHeader(
        className="site-page-header",
        onBack=lambda: None,
        title="Title",
        subTitle="This is a subtitle",
    )
