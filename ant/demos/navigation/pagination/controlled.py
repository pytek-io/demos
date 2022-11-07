import reflect as r
import reflect_antd as antd
import reflect_html as html


def app():
    pagination = antd.Pagination(defaultCurrent=3, total=50)
    r.autorun(lambda: print(pagination()))
    return pagination
