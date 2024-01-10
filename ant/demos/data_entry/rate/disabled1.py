import render_antd as antd
import render_html as html


def app(_):
    return html.div([antd.Rate(disabled=True, defaultValue=2)])
