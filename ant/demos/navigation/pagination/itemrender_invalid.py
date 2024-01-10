import render as r
import render_antd as antd

itemRender = r.JSMethod(
    "itemRender",
"""
if (type === 'prev') {
    return <a>Previous</a>;
}
if (type === 'next') {
    return <a>Next</a>;
}
return originalElement;
""",
    "_",
    "type",
    "originalElement",
)


def app(_):
    return antd.Pagination(
        total=500,
        itemRender=itemRender,
    )
