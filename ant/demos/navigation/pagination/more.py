import render_antd as antd
import render_html as html


def app(_):
    return html.div([antd.Pagination(defaultCurrent=6, total=500)])
