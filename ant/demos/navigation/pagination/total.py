import reflect as r
import reflect_antd as antd
import reflect_html as html

showTotal = r.JSMethod(
    "total",
    "return `Total ${total}  items`",
    "total",
)


showRange = r.JSMethod(
    "total_range",
    "return `${range[0]}-${range[1]} of ${total} items`",
    "total",
    "range",
)

def app():
    return html.div(
        [
            antd.Pagination(
                total=85, showTotal=showTotal, defaultPageSize=20, defaultCurrent=1
            ),
            html.br(),
            antd.Pagination(
                total=85, showTotal=showRange, defaultPageSize=20, defaultCurrent=1
            ),
        ]
    )
