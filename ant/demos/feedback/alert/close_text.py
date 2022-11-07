import reflect_antd as antd
import reflect_html as html


def app():
    return antd.Alert(message="Info Text", type="info", closeText="Close Now")
