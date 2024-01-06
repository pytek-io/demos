import render as r
import render_antd as antd
import render_html as html


def onChange(pageNumber):
    print("Page: ", pageNumber)


def app():
    pagination1 = antd.Pagination(showQuickJumper=True, defaultCurrent=2, total=500)
    r.autorun(lambda: print("Page: ", pagination1()))
    pagination2 = antd.Pagination(
        showQuickJumper=True, defaultCurrent=2, total=500, disabled=True
    )
    r.autorun(lambda: print("Page: ", pagination2()))
    return html.div([pagination1, html.br(), pagination2])
