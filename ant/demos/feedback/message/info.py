import reflect_antd as antd
import reflect_html as html


def info():
    antd.message.info("This is a normal message")


def app():
    return antd.Button("Display normal message", type="primary", onClick=info)
