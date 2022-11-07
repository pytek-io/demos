import reflect_antd as antd
import reflect_html as html


def app():
    return html.div(
        [antd.BackTop(), html.strong("gray", className="site-back-top-basic")]
    )
