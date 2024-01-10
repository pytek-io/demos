import render_antd as antd
import render_html as html


def showTotal():
    return f"Total {total} items"


def app(_):
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
