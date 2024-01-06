import render_antd as antd
import render_html as html


def onShowSizeChange(current, pageSize):
    print(current, pageSize)


def app():
    return html.div(
        [
            antd.Pagination(
                showSizeChanger=True,
                onShowSizeChange=onShowSizeChange,
                defaultCurrent=3,
                total=500,
            ),
            html.br(),
            antd.Pagination(
                showSizeChanger=True,
                onShowSizeChange=onShowSizeChange,
                defaultCurrent=3,
                total=500,
                disabled=True,
            ),
        ]
    )
