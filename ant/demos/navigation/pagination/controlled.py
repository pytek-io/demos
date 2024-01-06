import render as r
import render_antd as antd
import render_html as html


def app():
    pagination = antd.Pagination(defaultCurrent=3, total=50)
    r.autorun(lambda: print(pagination()))
    return pagination
