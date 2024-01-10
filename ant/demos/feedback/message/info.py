import render_antd as antd
import render_html as html


def info():
    antd.message.info("This is a normal message")


def app(_):
    return antd.Button("Display normal message", type="primary", onClick=info)
