import render as r
import render_antd as antd
import render_html as html

showTotal = r.js_arrow("total", "(total) => `Total ${total}  items`")
showRange = r.js_arrow(
    "total_range", "(total, range) => `${range[0]}-${range[1]} of ${total} items`"
)


def app(_):
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
