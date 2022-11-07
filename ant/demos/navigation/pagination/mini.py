import reflect_antd as antd
import reflect_html as html


def showTotal():
    return f"Total {total} items"


def app():
    return html.div(
        [
            antd.Pagination(size="small", total=50),
            antd.Pagination(
                size="small", total=50, showSizeChanger=True, showQuickJumper=True
            ),
            antd.Pagination(size="small", total=50),
            antd.Pagination(
                size="small",
                total=50,
                disabled=True,
                showSizeChanger=True,
                showQuickJumper=True,
            ),
        ]
    )
