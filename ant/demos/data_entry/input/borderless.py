import render_antd as antd
import render_html as html


def app():
    return antd.Input(placeholder="Borderless", bordered=False)
