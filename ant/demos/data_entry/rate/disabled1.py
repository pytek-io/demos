import reflect_antd as antd
import reflect_html as html


def app():
    return html.div([antd.Rate(disabled=True, defaultValue=2)])
