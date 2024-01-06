import render_antd as antd
import render_html as html


def app():
    return html.div(antd.Spin(), className="example")
