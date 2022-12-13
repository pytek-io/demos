import reflect_antd as antd
import reflect_html as html


def app():
    return antd.FloatButton(tooltip=html.div("Documents"))
