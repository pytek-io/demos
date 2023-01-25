import reflect as r
import reflect_antd as antd

showTotal = r.JSMethod(
    "total",
    "return `Total ${total}  items`",
    "total",
)


def app():
    return antd.Pagination(
        total=85, showTotal=showTotal, showSizeChanger=True, showQuickJumper=True
    )
