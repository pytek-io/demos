import render_antd as antd
import render_html as html


def app():
    return antd.Alert(message="Info Text", type="info", closeText="Close Now")
