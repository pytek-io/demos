import render as r
import render_antd as antd

showTotal = r.js_arrow("total", "(total) => `Total ${total}  items`")


def app(_):
    return antd.Pagination(
        total=85, showTotal=showTotal, showSizeChanger=True, showQuickJumper=True
    )
