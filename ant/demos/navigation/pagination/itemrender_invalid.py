import reflect as r
import reflect_antd as antd

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


def app():
    return antd.Pagination(
        total=500,
        itemRender=itemRender,
    )
