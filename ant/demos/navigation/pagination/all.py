import reflect as r
import reflect_antd as antd

showTotal = r.js_arrow("total", "(total) => `Total ${total}  items`")


def app():
    return antd.Pagination(
        total=85, showTotal=showTotal, showSizeChanger=True, showQuickJumper=True
    )
